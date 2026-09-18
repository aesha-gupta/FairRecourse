import argparse
import pandas as pd
from src.data_loader import load_and_preprocess_german_credit, load_and_preprocess_heloc
from src.model import CalibratedRiskModel
from src.explain import ExplainerEngine
from src.recourse import ConstrainedRecourseGenerator
from src.baseline import UnconstrainedBaselineRecourse
from src.policy_layer import PolicyAndConstraintLayer
from src.cost_feasibility import RecourseEvaluator
from src.certificate import generate_recourse_certificate
from src.monitoring import ModelMonitor


def main(applicant_id: int | None, dataset: str = "german"):
    print("\n" + "=" * 80)
    print(f"      FAIRRECOURSE: COMPARATIVE AUDIT [{dataset.upper()} BENCHMARK]")
    print("=" * 80)

    # 1. Pipeline Setup & Distribution Drift
    print(f"\n[1/4] Ingesting {dataset.upper()} dataset & calibrating LightGBM...")
    if dataset.lower() == "heloc":
        X_train, X_test, y_train, y_test, _, _ = load_and_preprocess_heloc()
        monitor_feature = "NetFractionRevolvingBurden"
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

    # Local TreeSHAP local attribution
    explainer = ExplainerEngine(risk_model, X_train)
    top_drivers = explainer.explain_instance(instance, top_k=3).to_dict(orient="records")

    # 3. Solve Counterfactuals
    print("[3/4] Solving counterfactuals via Baseline (Unconstrained) vs FairRecourse (PCL)...")
    pcl = PolicyAndConstraintLayer()
    evaluator = RecourseEvaluator()

    base_gen = UnconstrainedBaselineRecourse(risk_model.calibrated_model, X_train, list(X_train.columns))
    fair_gen = ConstrainedRecourseGenerator(risk_model.calibrated_model, X_train, list(X_train.columns), dataset_name=dataset)
    base_raw = base_gen.generate(instance, total_cfs=1)
    fair_raw = fair_gen.generate(instance, pcl=pcl, total_cfs=1,evaluator=evaluator)

    if fair_raw is None or fair_raw.empty:
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
        print("Recourse Assessment: Levers within permitted scope cannot offset these base bureau anchors.")
        print("Action: Escalate to credit committee for manual discretionary underwriting.")
        print("=" * 80 + "\n")
        return

    base_cf = base_raw.iloc[0].drop(labels=["target"], errors="ignore")
    fair_cf = fair_raw.iloc[0].drop(labels=["target"], errors="ignore")

    _, viol_base = pcl.validate(base_series, base_cf)
    eval_base = evaluator.evaluate(base_series, base_cf, viol_base)

    _, viol_fair = pcl.validate(base_series, fair_cf)
    eval_fair = evaluator.evaluate(base_series, fair_cf, viol_fair)

# 5. Stability Assessment
    cf_df = fair_raw.drop(columns=["target"], errors="ignore")
    stability_res = ModelMonitor.evaluate_recourse_stability(
        risk_model.calibrated_model,
        cf_df,
        original_instance=instance,
        threshold=0.40,
    )

    # 6. Render Comparative Output
    print("\n[4/4] GENERATING COMPARATIVE RECOURSE EVALUATION")
    print("=" * 80)
    print(f"{'Audit Metric / Feature':<32} {'Baseline (Standard DiCE)':<24} {'FairRecourse (PCL + Stability)'}")
    print("-" * 80)
    print(f"{'Deterministic Feasibility':<32} {'PASSED' if eval_base['feasible'] else 'FAILED':<24} {'PASSED' if eval_fair['feasible'] else 'FAILED'}")
    print(f"{'Feasibility Score [0-1]':<32} {eval_base['feasibility_score']:<24} {eval_fair['feasibility_score']}")
    print(f"{'Recourse Cost Metric':<32} {eval_base['recourse_cost']:<24} {eval_fair['recourse_cost']}")
    print(f"{'Execution Horizon (Months)':<32} {str(eval_base['months_required']) + ' mos':<24} {str(eval_fair['months_required']) + ' mos'}")
    print(f"{'Features Changed (Sparsity)':<32} {eval_base['sparsity']:<24} {eval_fair['sparsity']}")
    print(f"{'Epsilon-Stability':<32} {'Not Evaluated':<24} {stability_res['stability_rate'] * 100:.1f}% ({'STABLE' if stability_res['is_stable'] else 'SENSITIVE'})")
    print("-" * 80)

    if eval_base["violations"]:
        print("BASELINE VIOLATIONS CAUGHT BY PCL:")
        for v in eval_base["violations"]:
            print(f"  [X] {v}")
    if eval_fair["violations"]:
        print("FAIRRECOURSE VIOLATIONS:")
        for v in eval_fair["violations"]:
            print(f"  [X] {v}")
    if not eval_fair["violations"]:
        print("FAIRRECOURSE STATUS: PASSED (Zero Policy or Temporal Violations)")

    print("\n" + generate_recourse_certificate(
        audit_id=f"FR-2026-{dataset.upper()}-01",
        applicant_id=f"APP-{applicant_id:04d}",
        baseline_pd=prob,
        threshold=0.40,
        shap_drivers=top_drivers,
        baseline_profile=base_series.to_dict(),
        recourse_plan=fair_cf.to_dict(),
        eval_result=eval_fair,
    ))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run recourse audit")
    parser.add_argument("--applicant_id", type=int, default=None, help="Applicant index")
    parser.add_argument("--dataset", type=str, default="german", choices=["german", "heloc"], help="Dataset to audit")
    args = parser.parse_args()
    main(args.applicant_id, dataset=args.dataset)