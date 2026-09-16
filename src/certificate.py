def generate_recourse_certificate(
    audit_id: str,
    applicant_id: str,
    baseline_pd: float,
    threshold: float,
    shap_drivers: list,
    baseline_profile: dict,
    recourse_plan: dict,
    eval_result: dict,
) -> str:
    """Builds a formatted, human-readable Recourse Certificate."""
    constraint_status = "PASSED (Zero Violations)" if eval_result["feasible"] else "FAILED"
    if not eval_result["feasible"] and eval_result.get("violations"):
        violation_details = "\n" + "\n".join([f"  • Violation: {v}" for v in eval_result["violations"]])
    else:
        violation_details = ""

    lines = [
        "=" * 80,
        "                    FAIRRECOURSE UNDERWRITING AUDIT LOG                         ",
        "=" * 80,
        f"Audit Reference      : {audit_id}",
        f"Applicant Case ID    : {applicant_id}",
        f"Model Assessment     : Risk Threshold Exceeded",
        f"Calibrated PD        : {baseline_pd * 100:.1f}%  [Operational Threshold: {threshold * 100:.1f}%]",
        f"Recourse Target      : < {threshold * 100:.1f}%",
        "",
        "PRIMARY ADVERSE DETERMINATION DRIVERS (TreeSHAP Local Attribution)",
        "-" * 80,
    ]
    for d in shap_drivers:
        lines.append(f"• {d['feature']:<25} : {d['shap_value']:+.4f} margin [{d['risk_direction']}]")

    lines.extend([
        "",
        "FEASIBILITY-OPTIMIZED RECOURSE INTERVENTION",
        "-" * 80,
        f"{'Variable':<22} {'Current Value':<18} {'Target Recourse':<18} {'Intervention Plan'}",
        "-" * 80,
        f"{'Loan Duration':<22} {str(baseline_profile.get('duration_months')) + ' mos':<18} {str(recourse_plan.get('duration_months')) + ' mos':<18} Restructure Tenure",
        f"{'Revolving Debt':<22} {'€' + str(baseline_profile.get('revolving_debt')):<18} {'€' + str(recourse_plan.get('revolving_debt')):<18} Pay down balance",
        f"{'Savings Balance':<22} {'€' + str(baseline_profile.get('savings_balance')):<18} {'€' + str(recourse_plan.get('savings_balance')):<18} Accumulate liquidity",
        "-" * 80,
        "",
        "RECOURSE FEASIBILITY & TEMPORAL AUDIT",
        "-" * 80,
        f"Estimated Execution Horizon   : {eval_result['months_required']} Months",
        f"Monthly Commitment Required   : €{eval_result['monthly_commitment']:.2f} / month",
        f"Total Financial Shift         : €{eval_result['total_financial_shift']:.2f}",
        f"Composite Recourse Cost       : {eval_result['recourse_cost']}",
        f"Feasibility Score             : {eval_result['feasibility_score']} / 1.000",
        f"Deterministic Constraint Check: {constraint_status}{violation_details}",
        "",
        "DISCLAIMER: This certificate reports the mathematical criteria required to satisfy",
        "the calibrated risk model. It does not constitute a legally binding credit offer;",
        "final underwriting is subject to human-in-the-loop audit and regulatory compliance.",
        "=" * 80,
    ])
    return "\n".join(lines)