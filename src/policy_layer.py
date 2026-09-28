import pandas as pd
import json
import os


class PolicyAndConstraintLayer:
    """
    Robust compliance gatekeeper enforcing directional monotonicity, 
    immutability, and boundary rules across German Credit and HELOC.
    """

    def __init__(self, config_path=None, immutable_features=None, adverse_metrics=None, positive_metrics=None):
        if config_path is None:
            config_path = os.path.join(os.path.dirname(__file__), "..", "config", "default_schema.json")
            
        try:
            with open(config_path, 'r') as f:
                config = json.load(f)
            self.immutable_keywords = config.get("IMMUTABLE_KEYWORDS", [])
            self.adverse_metrics = config.get("ADVERSE_METRICS", [])
            self.positive_metrics = config.get("POSITIVE_METRICS", [])
        except (FileNotFoundError, json.JSONDecodeError):
            self.immutable_keywords = []
            self.adverse_metrics = []
            self.positive_metrics = []

        if immutable_features is not None:
            self.immutable_keywords = immutable_features
        if adverse_metrics is not None:
            self.adverse_metrics = adverse_metrics
        if positive_metrics is not None:
            self.positive_metrics = positive_metrics

    def validate(self, original_profile: pd.Series, counterfactual_profile: pd.Series) -> tuple[bool, list[str]]:
        violations = []

        for col in original_profile.index:
            if col in ["target", "risk_tier"] or col not in counterfactual_profile.index:
                continue

            # Safe numeric coercion; if string categorical, check immutability only
            try:
                old_val = float(original_profile[col])
                new_val = float(counterfactual_profile[col])
                is_numeric = True
            except (ValueError, TypeError):
                is_numeric = False
                if str(original_profile[col]) != str(counterfactual_profile[col]):
                    violations.append(f"Categorical mutation violation: Cannot alter {col} ({original_profile[col]} -> {counterfactual_profile[col]}).")
                continue

            col_lower = col.lower()

            # 1. Immutability Check
            if any(k in col_lower for k in self.immutable_keywords):
                if abs(new_val - old_val) > 1e-4:
                    violations.append(f"Immutability violation: Cannot alter historical/demographic feature {col} ({old_val:.2f} -> {new_val:.2f}).")

            # 2. Positive Credit Quality Metrics (Must NOT decrease)
            elif any(k in col_lower for k in self.positive_metrics):
                if new_val < old_val - 1e-4:
                    violations.append(f"Monotonicity violation: Quality metric {col} cannot decrease ({old_val:.2f} -> {new_val:.2f}).")

            # 3. Adverse Risk Metrics & Specific Delinquencies (Must NOT increase)
            elif any(k in col_lower for k in self.adverse_metrics) or ("delq" in col_lower and "never" not in col_lower):
                if new_val > old_val + 1e-4:
                    violations.append(f"Monotonicity violation: Adverse risk metric {col} cannot increase ({old_val:.2f} -> {new_val:.2f}).")

            # 4. Discrete Counts (Tolerant check for floating point precision)
            if col_lower.startswith("num"):
                if abs(new_val - round(new_val)) > 1e-3:
                    violations.append(f"Discrete count violation: {col} must be an integer, received {new_val:.2f}.")

            # 5. Physical Percentage Bounds [0, 100]
            if "percent" in col_lower or "fraction" in col_lower:
                if new_val < -1e-4 or new_val > 100.0001:
                    violations.append(f"Domain bounds violation: {col} must be within [0, 100]%, received {new_val:.2f}%.")

        return (len(violations) == 0, violations)

def compute_exposure_counter_offer(
    calibrated_pd: float, 
    operational_threshold: float = 0.40, 
    min_viable_ratio: float = 0.80
) -> dict:
    """
    Computes scale-invariant exposure scaling ratio alpha* = tau / PD.
    Preserves institutional Expected Loss without requiring unobserved loan amounts.
    """
    if calibrated_pd <= operational_threshold:
        return {
            "eligible": True,
            "scaling_ratio": 1.0,
            "haircut_pct": 0.0,
            "status": "APPROVED"
        }

    alpha = operational_threshold / calibrated_pd

    if alpha >= min_viable_ratio:
        haircut = round((1.0 - alpha) * 100, 2)
        return {
            "eligible": True,
            "scaling_ratio": round(alpha, 4),
            "haircut_pct": haircut,
            "status": "OPTION_A_COUNTER_OFFER",
            "statutory_notice": (
                f"Approved under an Exposure Scaling Cap of {alpha*100:.1f}% "
                f"({haircut}% facility limit haircut) preserving portfolio risk neutral tolerance."
            )
        }
    else:
        return {
            "eligible": False,
            "scaling_ratio": round(alpha, 4),
            "status": "RECOURSE_INFEASIBLE_COMMITTEE_ESCALATION",
            "statutory_notice": (
                f"Required exposure reduction ({(1.0 - alpha)*100:.1f}%) exceeds viable "
                f"contractual threshold ({int((1.0 - min_viable_ratio)*100)}%). Escalated to credit committee."
            )
        }