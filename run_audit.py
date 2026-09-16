import argparse
import pandas as pd
from src.data_loader import load_and_preprocess_german_credit, load_and_preprocess_heloc
from src.model import CalibratedRiskModel
from src.explain import ExplainerEngine
from src.recourse import ConstrainedRecourseGenerator
from src.policy_layer import PolicyAndConstraintLayer
from src.cost_feasibility import RecourseEvaluator
from src.audit import FairnessAuditor
from src.certificate import generate_recourse_certificate
from src.sensitivity import run_threshold_sensitivity
from src.monitoring import ModelMonitor


def main(applicant_id: int | None, dataset: str = "german"):
    print(f"\n[1/5] Loading {dataset.upper()} benchmark dataset...")
    if dataset.lower() == "heloc":
        X_train, X_test, y_train, y_test, A_train, A_test = load_and_preprocess_heloc()
        monitor_feature = "NetFractionRevolvingBurden"
        protected_col = "risk_tier"
        privileged_grp = "Higher_Score_Tier"
        unprivileged_grp = "Lower_Score_Tier"
    else:
        X_train, X_test, y_train, y_test, A_train, A_test = load_and_preprocess_german_credit()
        monitor_feature = "savings_balance"
        protected_col = "gender"
        privileged_grp = "Male"
        unprivileged_grp = "Female"

    # Distribution Stability (PSI)
    psi_val = ModelMonitor.calculate_psi(X_train[monitor_feature], X_test[monitor_feature])
    drift_status = "STABLE" if psi_val < 0.10 else "MODERATE/HIGH DRIFT"
    print(f"      Distribution Stability ({monitor_feature} PSI): {psi_val} [{drift_status}]")

    print(f"[2/5] Training Calibrated LightGBM model on {dataset.upper()}...")
    risk_model = CalibratedRiskModel().fit(X_train, y_train)
    metrics = risk_model.evaluate(X_test, y_test)
    print(f"      Model Quality: ROC-AUC={metrics['roc_auc']}, PR-AUC={metrics['pr_auc']}, Brier={metrics['brier_score']}")

    # Auto-select adverse profile if unspecified
    if applicant_id is None:
        test_probs = risk_model.predict_proba(X_test)
        rejected_indices = [i for i, p in enumerate(test_probs) if p >= 0.40]
        if not rejected_indices:
            print("No rejected applicants found in test set at 40% threshold.")
            return
        applicant_id = rejected_indices[0]
        print(f"      Auto-selected first rejected applicant ID: #{applicant_id}")

    instance = X_test.iloc[[applicant_id]]
    prob = risk_model.predict_proba(instance)[0]
    print(f"\n[3/5] Evaluating Applicant ID #{applicant_id}: Calibrated Default PD = {prob * 100:.2f}%")

    if prob < 0.40:
        print(f"      Applicant #{applicant_id} is Approved (PD < 40%). Recourse search skipped.")
        return

    print("      Adverse outcome identified. Computing TreeSHAP local attributions...")
    explainer = ExplainerEngine(risk_model, X_train)
    top_drivers = explainer.explain_instance(instance, top_k=3).to_dict(orient="records")

    print("[4/5] Generating constrained counterfactual recourse via DiCE & PCL...")
    recourse_gen = ConstrainedRecourseGenerator(
        risk_model.calibrated_model, X_train, continuous_features=list(X_train.columns)
    )
    raw_cfs = recourse_gen.generate(instance, total_cfs=1)

    if raw_cfs is None or raw_cfs.empty:
        print(f"\n" + "=" * 80)
        print(f"AUDIT ASSESSMENT: RECOURSE INFEASIBLE FOR APPLICANT #{applicant_id}")
        print("=" * 80)
        print(f"Calibrated Default Risk: {prob * 100:.2f}% (Threshold: 40.0%)")
        print("No mathematically valid counterfactual path exists within actionable domain limits.")
        print("Action: Escalate to Senior Underwriter (Manual Exception Review).")
        print("=" * 80 + "\n")
        return

    target_cf = raw_cfs.iloc[0].drop(labels=["target"], errors="ignore")
    
    # Policy & constraint validation
    pcl = PolicyAndConstraintLayer()
    baseline_series = instance.iloc[0]
    is_valid, violations = pcl.validate(baseline_series, target_cf)

    # Cost and feasibility evaluation
    evaluator = RecourseEvaluator()
    feasibility_res = evaluator.evaluate(baseline_series, target_cf, violations)

    # Recourse Epsilon-Stability Check
    stability_res = ModelMonitor.evaluate_recourse_stability(
        risk_model, pd.DataFrame([target_cf]), threshold=0.40
    )

    print("[5/5] Generating Auditable Recourse Certificate...\n")
    cert = generate_recourse_certificate(
        audit_id=f"FR-2026-{dataset.upper()}-AUDIT",
        applicant_id=f"APP-{applicant_id:04d}",
        baseline_pd=prob,
        threshold=0.40,
        shap_drivers=top_drivers,
        baseline_profile=baseline_series.to_dict(),
        recourse_plan=target_cf.to_dict(),
        eval_result=feasibility_res,
    )
    print(cert)

    print("RECOURSE ROBUSTNESS EVALUATION:")
    print(f"• Epsilon-Stability Score : {stability_res['stability_rate'] * 100:.1f}%")
    print(f"• Robustness Status       : {'ROBUST' if stability_res['is_stable'] else 'PERTURBATION-SENSITIVE'}")

    # Fairness summary
    auditor = FairnessAuditor(y_test, risk_model.predict_proba(X_test), A_test[protected_col])
    fairness = auditor.run_predictive_audit(privileged_group=privileged_grp, unprivileged_group=unprivileged_grp)
    print(f"\nDEMOGRAPHIC EQUITY SUMMARY ({protected_col.title()} Audit):")
    for k, v in fairness.items():
        print(f"• {k}: {v}")

    # Sensitivity overview
    sens_df = run_threshold_sensitivity(risk_model, X_test)
    print("\nOPERATIONAL THRESHOLD SENSITIVITY:")
    print(sens_df.to_string(index=False))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="FairRecourse CLI Audit")
    parser.add_argument("--applicant_id", type=int, default=None, help="Index of test applicant to evaluate")
    parser.add_argument("--dataset", type=str, default="german", choices=["german", "heloc"], help="Dataset to audit")
    args = parser.parse_args()
    main(args.applicant_id, dataset=args.dataset)