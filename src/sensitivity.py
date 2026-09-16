import numpy as np
import pandas as pd


def run_threshold_sensitivity(model, X_test: pd.DataFrame, thresholds: list = None) -> pd.DataFrame:
    """Evaluates the approval and default impact across a range of decision thresholds tau."""
    thresholds = thresholds or [0.30, 0.40, 0.50, 0.60]
    probs = model.predict_proba(X_test)
    results = []

    for t in thresholds:
        approvals = (probs < t).sum()
        approval_rate = approvals / len(X_test)
        results.append({
            "threshold_tau": t,
            "approval_count": approvals,
            "approval_rate": round(float(approval_rate), 3),
            "mean_accepted_pd": round(float(probs[probs < t].mean()), 4) if approvals > 0 else 0.0,
        })

    return pd.DataFrame(results)