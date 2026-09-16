import pandas as pd


class PolicyAndConstraintLayer:
    """Enforces deterministic domain, immutability, and causal financial accounting rules."""
    def __init__(self, immutable_features: list = None):
        self.immutable_features = immutable_features or [
            "installment_rate", "present_residence_since",
            "people_liable", "monthly_income", "disposable_income"
        ]

    def validate(self, baseline: pd.Series, candidate: pd.Series) -> tuple[bool, list[str]]:
        violations = []

        # 1. Immutability checks
        for feat in self.immutable_features:
            if feat in candidate and candidate[feat] != baseline[feat]:
                violations.append(f"Immutable feature violated: {feat} changed from {baseline[feat]} to {candidate[feat]}")

        # 2. Monotonicity bounds
        if candidate.get("savings_balance", 0.0) < baseline.get("savings_balance", 0.0):
            violations.append("Monotonicity violation: Savings cannot decrease for positive recourse.")

        if candidate.get("revolving_debt", 0.0) > baseline.get("revolving_debt", 0.0):
            violations.append("Monotonicity violation: Debt accumulation cannot resolve credit risk.")

        # 3. Domain boundaries
        if candidate.get("duration_months", 0) < 6:
            violations.append("Domain bounds violation: Minimum loan tenure is 6 months.")

        # 4. Causal Financial Reality Check (Duration vs. Installment)
        # If duration drops significantly, installment burden must not stay artificially low
        base_dur = baseline.get("duration_months", 24)
        cand_dur = candidate.get("duration_months", 24)
        if cand_dur < base_dur * 0.70 and candidate.get("installment_rate") == baseline.get("installment_rate"):
            violations.append(
                f"Causal coupling violation: Tenure shortened from {base_dur}m to {cand_dur}m without adjusting installment amortisation capacity."
            )

        is_valid = len(violations) == 0
        return is_valid, violations