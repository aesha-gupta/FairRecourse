"""
Unit tests ensuring immutable features cannot be modified
"""
import pytest
import pandas as pd
from src.policy_layer import PolicyAndConstraintLayer


def test_immutable_feature_modification():
    pcl = PolicyAndConstraintLayer(immutable_features=["monthly_income"])
    baseline = pd.Series({"monthly_income": 3000.0, "savings_balance": 500.0, "revolving_debt": 2000.0})
    candidate = pd.Series({"monthly_income": 4500.0, "savings_balance": 500.0, "revolving_debt": 2000.0})

    valid, violations = pcl.validate(baseline, candidate)
    assert valid is False
    assert any("monthly_income" in v for v in violations)


def test_valid_recourse():
    pcl = PolicyAndConstraintLayer()
    baseline = pd.Series({
        "installment_rate": 4, "present_residence_since": 2, "people_liable": 1,
        "monthly_income": 3000.0, "disposable_income": 800.0,
        "savings_balance": 500.0, "revolving_debt": 2000.0, "duration_months": 36
    })
    candidate = pd.Series({
        "installment_rate": 4, "present_residence_since": 2, "people_liable": 1,
        "monthly_income": 3000.0, "disposable_income": 800.0,
        "savings_balance": 1200.0, "revolving_debt": 1000.0, "duration_months": 24
    })

    valid, violations = pcl.validate(baseline, candidate)
    assert valid is True
    assert len(violations) == 0