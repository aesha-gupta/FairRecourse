"""
Tests verifying monotonicity (e.g., savings cannot decrease)
"""
import pytest
import pandas as pd
from src.policy_layer import PolicyAndConstraintLayer


def test_negative_savings_violation():
    pcl = PolicyAndConstraintLayer()
    baseline = pd.Series({"savings_balance": 1500.0, "revolving_debt": 1000.0})
    candidate = pd.Series({"savings_balance": 800.0, "revolving_debt": 500.0})

    valid, violations = pcl.validate(baseline, candidate)
    assert valid is False
    assert any("cannot decrease" in v for v in violations)


def test_debt_increase_violation():
    pcl = PolicyAndConstraintLayer()
    baseline = pd.Series({"savings_balance": 1000.0, "revolving_debt": 1000.0})
    candidate = pd.Series({"savings_balance": 2000.0, "revolving_debt": 1500.0})

    valid, violations = pcl.validate(baseline, candidate)
    assert valid is False
    assert any("cannot increase" in v for v in violations)