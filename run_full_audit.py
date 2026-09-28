import argparse
import pandas as pd
from src.data_loader import load_and_preprocess_german_credit, load_and_preprocess_heloc, load_and_preprocess_cibil
from src.model import CalibratedRiskModel
from src.explain import ExplainerEngine
from src.recourse import ConstrainedRecourseGenerator
from src.baseline import UnconstrainedBaselineRecourse
from src.policy_layer import PolicyAndConstraintLayer, compute_exposure_counter_offer
from src.cost_feasibility import RecourseEvaluator
from src.certificate import generate_recourse_certificate
from src.monitoring import ModelMonitor

# Explicit feature partitions for the two pathways
CONTRACTUAL_LEVERS = ["duration_months", "credit_amount", "installment_rate"]
BALANCE_SHEET_LEVERS = [
    "savings_balance", "revolving_debt", "CC_utilization", 
    "NetFractionRevolvingBurden", "NetFractionInstallBurden",
    "NumRevolvingTradesWBalance", "PL_utilization", "pct_currentBal_all_TL"
]


def main(applicant_id: int | None, dataset: str = "german"):
    print("\n" + "=" * 80)
    print(f"      FAIRRECOURSE: COMPARATIVE AUDIT [{dataset.upper()} BENCHMARK]")
    print("=" * 80)
    
    currency_map = {"german": "\u20AC", "heloc": "$", "cibil": "\u20B9"}
    curr_sym = currency_map.get(dataset.lower(), "")

    # 1. Pipeline Setup & Distribution Drift
    print(f"\n[1/4] Ingesting {dataset.upper()} dataset & calibrating LightGBM...")
    if dataset.lower() == "heloc":
        X_train, X_test, y_train, y_test, _, _ = load_and_preprocess_heloc()
        monitor_feature = "NetFractionRevolvingBurden"
    elif dataset.lower() == "cibil":
        X_train, X_test, y_train, y_test, _, _ = load_and_preprocess_cibil()
        monitor_feature = "CC_utilization"
    else:
        X_train, X_test, y_train, y_test, _, _ = load_and_preprocess_german_credit()
        monitor_feature = "savings_balance"

    risk_model = CalibratedRiskModel().fit(X_train, y_train)
    metrics = risk_model.evaluate(X_test, y_test)
    print(f"      Model Quality ({dataset.upper()}): ROC-AUC={metrics['roc_auc']}, PR-AUC={metrics['pr_auc']}, Brier={metrics['brier_score']}")

    psi_score = ModelMonitor.calculate_psi(X_train[monitor_feature], X_test[monitor_feature])
    print(f"      Distribution Stability ({monitor_feature} PSI): {psi_score}")

    # 2. Select Adverse Applicant
    if applicant_id is None:
        probs = risk_model.predict_proba(X_test)
        rejected_indices = [i for i, p in enumerate(probs) if p >= 0.40]
        if not rejected_indices:
            print("No adverse applicants found at threshold = 0.40.")
            return
        applicant_id = rejected_indices[0]

    instance = X_test.iloc[[applicant_id]]
    prob = risk_model.predict_proba(instance)[0]
    base_series = instance.iloc[0]

    print(f"[2/4] Selected Applicant ID #{applicant_id} | Calibrated PD: {prob * 100:.2f}% (Threshold: 40.0%)")
    if prob < 0.40:
        print("      Applicant is within approved risk limits. Recourse search skipped.")
        return

    # Local TreeSHAP attribution
    explainer = ExplainerEngine(risk_model, X_train)
    top_drivers = explainer.explain_instance(instance, top_k=3).to_dict(orient="records")

    # 3. Solve Counterfactuals (Baseline vs Dual Pathways)
    print("[3/4] Solving counterfactuals via Baseline vs FairRecourse Dual Pathways...")
    pcl = PolicyAndConstraintLayer()
    evaluator = RecourseEvaluator()

    # Unconstrained Baseline (DiCE-style)
    base_gen = UnconstrainedBaselineRecourse(risk_model.calibrated_model, X_train, list(X_train.columns))
    base_raw = base_gen.generate(instance, total_cfs=1)

    # FairRecourse Generator
    fair_gen = ConstrainedRecourseGenerator(
        risk_model.calibrated_model, X_train, list(X_train.columns), dataset_name=dataset
    )

    # --- OPTION A: Contractual Levers (tenure, amount) ---
    fair_raw_a = fair_gen.generate(
        instance, pcl=pcl, total_cfs=1, evaluator=evaluator, allowed_features=CONTRACTUAL_LEVERS, max_active_levers=3
    )

    # --- OPTION B: Balance-Sheet Levers (savings, revolving debt, utilization) ---
    fair_raw_b = fair_gen.generate(
        instance, pcl=pcl, total_cfs=1, evaluator=evaluator, allowed_features=BALANCE_SHEET_LEVERS, max_active_levers=3
    )

    # Deep Infeasibility check: If BOTH pathways fail, escalate to human committee
    if (fair_raw_a is None or fair_raw_a.empty) and (fair_raw_b is None or fair_raw_b.empty):
        print("\n" + "=" * 80)
        print(f"AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE FOR APPLICANT #{applicant_id}")
        print("=" * 80)
        print(f"Calibrated Default Risk: {prob * 100:.2f}% (Threshold: 40.0%)")
        print("\nPRIMARY ADVERSE DETERMINATION DRIVERS (TreeSHAP Root Cause Analysis):")
        print("-" * 80)
        for driver in top_drivers:
            feature = driver.get("feature", driver.get("column", "Unknown"))
            impact = driver.get("attribution", driver.get("shap_value", 0.0))
            print(f"  • {feature:<35} : +{impact:.4f} margin [Increases Default Risk]")
        print("-" * 80)
        print("Recourse Assessment: Levers within permitted scope cannot offset base bureau anchors.")
        print("Action: Escalate to credit committee for manual discretionary underwriting.")
        counter_offer = compute_exposure_counter_offer(prob)
        print(f"-> EXPOSURE SCALING ANALYSIS: {counter_offer['statutory_notice']}")
        print("=" * 80 + "\n")

    # Baseline evaluation
    base_cf = base_raw.iloc[0].drop(labels=["target"], errors="ignore")
    _, viol_base = pcl.validate(base_series, base_cf)
    eval_base = evaluator.evaluate(base_series, base_cf, viol_base)

    # Evaluate Option A if passed
    eval_fair_a, stability_a = None, None
    if fair_raw_a is not None and not fair_raw_a.empty:
        fair_cf_a = fair_raw_a.iloc[0].drop(labels=["target"], errors="ignore")
        _, viol_a = pcl.validate(base_series, fair_cf_a)
        eval_fair_a = evaluator.evaluate(base_series, fair_cf_a, viol_a)
        cf_df_a = fair_raw_a.drop(columns=["target"], errors="ignore")
        stability_a = ModelMonitor.evaluate_recourse_stability(
            risk_model.calibrated_model, cf_df_a, original_instance=instance, threshold=0.40
        )

    # Evaluate Option B if passed
    eval_fair_b, stability_b = None, None
    if fair_raw_b is not None and not fair_raw_b.empty:
        fair_cf_b = fair_raw_b.iloc[0].drop(labels=["target"], errors="ignore")
        _, viol_b = pcl.validate(base_series, fair_cf_b)
        eval_fair_b = evaluator.evaluate(base_series, fair_cf_b, viol_b)
        cf_df_b = fair_raw_b.drop(columns=["target"], errors="ignore")
        stability_b = ModelMonitor.evaluate_recourse_stability(
            risk_model.calibrated_model, cf_df_b, original_instance=instance, threshold=0.40
        )

    # 4. Render Comparative Output
    print("\n[4/4] GENERATING COMPARATIVE RECOURSE EVALUATION")
    print("=" * 88)
    print(f"{'Audit Metric / Feature':<28} {'Baseline (DiCE)':<18} {'FairRecourse (Opt A)':<22} {'FairRecourse (Opt B)'}")
    print("-" * 88)
    print(f"{'Pathway Classification':<28} {'Unconstrained':<18} {'Contractual':<22} {'Balance Sheet'}")
    
    feas_a = "PASSED" if eval_fair_a and eval_fair_a['feasible'] else "INFEASIBLE"
    feas_b = "PASSED" if eval_fair_b and eval_fair_b['feasible'] else "INFEASIBLE"
    print(f"{'Deterministic Feasibility':<28} {'PASSED' if eval_base['feasible'] else 'FAILED':<18} {feas_a:<22} {feas_b}")

    score_a = f"{eval_fair_a['feasibility_score']:.3f}" if eval_fair_a else "N/A"
    score_b = f"{eval_fair_b['feasibility_score']:.3f}" if eval_fair_b else "N/A"
    print(f"{'Feasibility Score [0-1]':<28} {eval_base['feasibility_score']:<18.3f} {score_a:<22} {score_b}")

    cost_a = f"{eval_fair_a['recourse_cost']:.3f}" if eval_fair_a else "N/A"
    cost_b = f"{eval_fair_b['recourse_cost']:.3f}" if eval_fair_b else "N/A"
    print(f"{'Recourse Cost Metric':<28} {eval_base['recourse_cost']:<18.3f} {cost_a:<22} {cost_b}")

    horiz_a = f"{eval_fair_a['months_required']} mos" if eval_fair_a else "N/A"
    horiz_b = f"{eval_fair_b['months_required']} mos" if eval_fair_b else "N/A"
    print(f"{'Execution Horizon':<28} {str(eval_base['months_required']) + ' mos':<18} {horiz_a:<22} {horiz_b}")

    stab_a = f"{stability_a['stability_rate']*100:.0f}%" if stability_a else "N/A"
    stab_b = f"{stability_b['stability_rate']*100:.0f}%" if stability_b else "N/A"
    print(f"{'Epsilon-Stability':<28} {'Not Evaluated':<18} {stab_a:<22} {stab_b}")
    print("-" * 88)

    if eval_base["violations"]:
        print("BASELINE VIOLATIONS CAUGHT BY PCL:")
        for v in eval_base["violations"]:
            print(f"  [X] {v}")

    # 5. Dual-Pathway Underwriting Certificates
    print("\n" + "=" * 80)
    print("                    FAIRRECOURSE ACTIONABLE PATHWAY CERTIFICATES")
    print("=" * 80)

    # Option A Certificate
    if eval_fair_a and eval_fair_a["feasible"]:
        print("\n>>> [OPTION A: CONTRACTUAL RESTRUCTURING CERTIFICATE]")
        print(generate_recourse_certificate(
            audit_id=f"FR-2026-{dataset.upper()}-OPT-A",
            applicant_id=f"APP-{applicant_id:04d}",
            baseline_pd=prob,
            threshold=0.40,
            shap_drivers=top_drivers,
            baseline_profile=base_series.to_dict(),
            recourse_plan=fair_cf_a.to_dict(),
            eval_result=eval_fair_a,
            currency_symbol=curr_sym,
        ))
    else:
        print("\n>>> [OPTION A: CONTRACTUAL RESTRUCTURING] -> INFEASIBLE")

    # Option B Certificate
    if eval_fair_b and eval_fair_b["feasible"]:
        print("\n>>> [OPTION B: BALANCE SHEET & LIQUIDITY CERTIFICATE]")
        print(generate_recourse_certificate(
            audit_id=f"FR-2026-{dataset.upper()}-OPT-B",
            applicant_id=f"APP-{applicant_id:04d}",
            baseline_pd=prob,
            threshold=0.40,
            shap_drivers=top_drivers,
            baseline_profile=base_series.to_dict(),
            recourse_plan=fair_cf_b.to_dict(),
            eval_result=eval_fair_b,
            currency_symbol=curr_sym,
        ))
    else:
        print("\n>>> [OPTION B: BALANCE SHEET & LIQUIDITY] -> INFEASIBLE (Exceeds 24-Month Solvency Horizon)")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run recourse audit")
    parser.add_argument("--applicant_id", type=int, default=None, help="Applicant index")
    parser.add_argument("--dataset", type=str, default="german", choices=["german", "heloc", "cibil"], help="Dataset to audit")
    args = parser.parse_args()
    main(args.applicant_id, dataset=args.dataset)