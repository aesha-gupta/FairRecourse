import numpy as np
import pandas as pd


class RecourseEvaluator:
    def __init__(self, max_horizon_months: float = 24.0, capacity_ratio: float = 0.25):
        self.max_horizon = max_horizon_months
        self.capacity_ratio = capacity_ratio

    def evaluate(self, baseline: pd.Series, candidate: pd.Series, violations: list | None = None) -> dict:
        active_violations = list(violations) if violations else []

        monthly_income = float(baseline.get("monthly_income", 2000.0))
        disposable_income = float(baseline.get("disposable_income", 600.0))
        monthly_budget = disposable_income * self.capacity_ratio

        delta_savings = max(0.0, float(candidate.get("savings_balance", 0.0)) - float(baseline.get("savings_balance", 0.0)))
        delta_debt_paydown = max(0.0, float(baseline.get("revolving_debt", 0.0)) - float(candidate.get("revolving_debt", 0.0)))
        total_financial_shift = delta_savings + delta_debt_paydown

        months_required = (total_financial_shift / monthly_budget) if monthly_budget > 0 else 99.0
        months_required = round(max(1.0, months_required), 1)

        # Check horizon constraint
        if months_required > self.max_horizon:
            active_violations.append(
                f"Exceeds max execution horizon ({months_required} > {self.max_horizon} months)"
            )

        l0_sparsity = sum(1 for col in baseline.index if candidate.get(col) != baseline.get(col))

        cost = (
            0.5 * (total_financial_shift / max(monthly_income, 1.0)) +
            0.3 * (months_required / 12.0) +
            0.2 * l0_sparsity
        )

        if active_violations:
            feasibility_score = 0.0
            feasible = False
        else:
            feasibility_score = float(np.clip(1.0 - (months_required / self.max_horizon), 0.05, 1.0))
            feasible = True

        return {
            "feasible": feasible,
            "feasibility_score": round(feasibility_score, 3),
            "recourse_cost": round(cost, 3),
            "months_required": months_required,
            "monthly_commitment": round(total_financial_shift / max(months_required, 1.0), 2),
            "total_financial_shift": round(total_financial_shift, 2),
            "sparsity": l0_sparsity,
            "violations": active_violations,
        }