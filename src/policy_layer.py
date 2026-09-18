import pandas as pd


class PolicyAndConstraintLayer:
    """
    Robust compliance gatekeeper enforcing directional monotonicity, 
    immutability, and boundary rules across German Credit and HELOC.
    """

    # Features that can never change
    IMMUTABLE_KEYWORDS = [
        "age", "sex", "gender", "personal_status", "foreign_worker",
        "msince", "averageminfile", "history", "delqever"
    ]

    # Metrics where higher value = MORE risk (must NOT increase)
    ADVERSE_METRICS = [
        "burden", "debt", "inq", "derog", "highutil", "util"
    ]

    # Metrics where higher value = LESS risk (must NOT decrease)
    POSITIVE_METRICS = [
        "savings", "percenttradesneverdelq", "clean", "asset"
    ]

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
            if any(k in col_lower for k in self.IMMUTABLE_KEYWORDS):
                if abs(new_val - old_val) > 1e-4:
                    violations.append(f"Immutability violation: Cannot alter historical/demographic feature {col} ({old_val:.2f} -> {new_val:.2f}).")

            # 2. Positive Credit Quality Metrics (Must NOT decrease)
            elif any(k in col_lower for k in self.POSITIVE_METRICS):
                if new_val < old_val - 1e-4:
                    violations.append(f"Monotonicity violation: Quality metric {col} cannot decrease ({old_val:.2f} -> {new_val:.2f}).")

            # 3. Adverse Risk Metrics & Specific Delinquencies (Must NOT increase)
            elif any(k in col_lower for k in self.ADVERSE_METRICS) or ("delq" in col_lower and "never" not in col_lower):
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