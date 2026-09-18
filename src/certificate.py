from typing import Any, Dict, List, Optional
import math


def _coerce_float(val: Any) -> Optional[float]:
    """Safely coerces numeric values to float, handling None, NaN, and strings."""
    if val is None:
        return None
    try:
        f = float(val)
        return None if math.isnan(f) else f
    except (ValueError, TypeError):
        return None


def _format_intervention_plan(feature: str, val_base: Any, val_target: Any) -> str:
    """Assigns an intuitive action label based on feature name and direction."""
    f_lower = feature.lower()
    b_num = _coerce_float(val_base)
    t_num = _coerce_float(val_target)

    # Calculate delta only if both values are valid floats
    delta = (t_num - b_num) if (b_num is not None and t_num is not None) else None

    if any(k in f_lower for k in ["debt", "burden", "delq", "utilization", "inq"]):
        return "Pay down balance / reduce utilization" if (delta is not None and delta <= 0) else "Restructure liability"
    if any(k in f_lower for k in ["duration", "month", "term"]):
        return "Restructure tenure"
    if any(k in f_lower for k in ["saving", "balance", "asset", "liquidity"]):
        return "Accumulate liquidity" if (delta is not None and delta >= 0) else "Reallocate reserves"
    if any(k in f_lower for k in ["trades", "num_"]):
        return "Consolidate active trade lines"
    return "Target parameter adjustment"


def _format_val(val: Any) -> str:
    """Formats numeric floats cleanly or returns clean string representations."""
    num = _coerce_float(val)
    if num is not None:
        return f"{num:.2f}"
    return "N/A" if val is None else str(val)


def generate_recourse_certificate(
    audit_id: str,
    applicant_id: str,
    baseline_pd: float,
    threshold: float,
    shap_drivers: List[Dict[str, Any]],
    baseline_profile: Dict[str, Any],
    recourse_plan: Dict[str, Any],
    eval_result: Dict[str, Any],
    currency_symbol: str = "",
) -> str:
    """
    Builds a robust, production-ready Recourse Certificate dynamic across 
    HELOC, German Credit, or arbitrary retail banking datasets.
    """
    constraint_status = "PASSED (Zero Violations)" if eval_result.get("feasible") else "FAILED"
    violations = eval_result.get("violations", [])
    violation_details = ("\n" + "\n".join([f"  • Violation: {v}" for v in violations])) if violations else ""

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
        f"{'Variable':<26} {'Current Value':<18} {'Target Recourse':<18} {'Intervention Plan'}",
        "-" * 80,
    ])

    # Preserve feature order while capturing union of keys
    all_keys = list(dict.fromkeys(list(baseline_profile.keys()) + list(recourse_plan.keys())))
    changes_found = False

    for k in all_keys:
        val_base = baseline_profile.get(k)
        val_target = recourse_plan.get(k)

        b_num = _coerce_float(val_base)
        t_num = _coerce_float(val_target)

        # Check numeric difference or categorical mismatch
        if b_num is not None and t_num is not None:
            is_diff = abs(b_num - t_num) > 1e-4
        else:
            is_diff = str(val_base) != str(val_target)

        if is_diff:
            changes_found = True
            action = _format_intervention_plan(k, val_base, val_target)
            lines.append(
                f"{k:<26} {_format_val(val_base):<18} {_format_val(val_target):<18} {action}"
            )

    if not changes_found:
        lines.append(
            f"{'No Feature Alterations':<26} {'N/A':<18} {'N/A':<18} No Viable Pathway"
        )

    # Unit formatting
    curr = f"{currency_symbol} " if currency_symbol else ""
    monthly_commit = eval_result.get("monthly_commitment", 0.0)
    fin_shift = eval_result.get("total_financial_shift", 0.0)

    lines.extend([
        "-" * 80,
        "",
        "RECOURSE FEASIBILITY & TEMPORAL AUDIT",
        "-" * 80,
        f"Estimated Execution Horizon   : {eval_result.get('months_required', 0.0)} Months",
        f"Monthly Commitment Required   : {curr}{monthly_commit:.2f} / month",
        f"Total Financial Shift         : {curr}{fin_shift:.2f}",
        f"Composite Recourse Cost       : {eval_result.get('recourse_cost', 0.0)}",
        f"Feasibility Score             : {eval_result.get('feasibility_score', 0.0)} / 1.000",
        f"Deterministic Constraint Check: {constraint_status}{violation_details}",
        "",
        "DISCLAIMER: This certificate reports the mathematical criteria required to satisfy",
        "the calibrated risk model. It does not constitute a legally binding credit offer;",
        "final underwriting is subject to human-in-the-loop audit and regulatory compliance.",
        "=" * 80,
    ])

    return "\n".join(lines)