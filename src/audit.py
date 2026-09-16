"""
DPR, EOD, calibration error, and recourse cost disparity (ΔC_rec)
"""
import numpy as np
import pandas as pd


class FairnessAuditor:
    def __init__(self, y_true: pd.Series, y_prob: np.ndarray, A_group: pd.Series, threshold: float = 0.40):
        self.df = pd.DataFrame({
            "y_true": y_true.values,
            "y_prob": y_prob,
            "group": A_group.values,
            "y_pred": (y_prob >= threshold).astype(int),
        })

    def run_predictive_audit(self, privileged_group: str = "Male", unprivileged_group: str = "Female") -> dict:
        priv = self.df[self.df["group"] == privileged_group]
        unpriv = self.df[self.df["group"] == unprivileged_group]

        # Approval rate is predicted non-default (y_pred == 0)
        app_rate_priv = (priv["y_pred"] == 0).mean()
        app_rate_unpriv = (unpriv["y_pred"] == 0).mean()
        dpr = (app_rate_unpriv / app_rate_priv) if app_rate_priv > 0 else 0.0

        # Equal Opportunity: TPR on approving good credit (y_true == 0)
        tpr_priv = (priv[priv["y_true"] == 0]["y_pred"] == 0).mean()
        tpr_unpriv = (unpriv[unpriv["y_true"] == 0]["y_pred"] == 0).mean()
        eod = abs(tpr_priv - tpr_unpriv)

        return {
            "privileged_approval_rate": round(app_rate_priv, 3),
            "unprivileged_approval_rate": round(app_rate_unpriv, 3),
            "demographic_parity_ratio": round(dpr, 3),
            "equal_opportunity_diff": round(eod, 3),
        }

    @staticmethod
    def calculate_recourse_disparity(recourse_costs_a: list, recourse_costs_b: list) -> dict:
        mean_a = float(np.mean(recourse_costs_a)) if len(recourse_costs_a) > 0 else 0.0
        mean_b = float(np.mean(recourse_costs_b)) if len(recourse_costs_b) > 0 else 0.0
        delta_c_rec = abs(mean_a - mean_b)
        return {
            "mean_cost_group_a": round(mean_a, 3),
            "mean_cost_group_b": round(mean_b, 3),
            "delta_c_recourse": round(delta_c_rec, 3),
        }