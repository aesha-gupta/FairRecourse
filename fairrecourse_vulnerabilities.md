# FairRecourse Vulnerability & Readiness Report

This report evaluates the readiness of the FairRecourse project for publication at **ACM FAccT (Conference on Fairness, Accountability, and Transparency)**. While the theoretical contributions (Policy Constraint Layer, Exposure Scaling, Temporal Solvency) are strong, the empirical implementation contains **critical vulnerabilities and failing tests** that undermine the validity of the experiments.

The project is **not ready** for submission until these issues are resolved.

---

## 1. Critical Vulnerabilities

### A. Pre-Split Data Leakage (Target/Distribution Leak)
- **Files Affected:** `src/data_loader.py` (Lines: `113-114` for HELOC, `187` for CIBIL)
- **The Issue:** The script computes distributional statistics (like `median_score` and `median_inc`) and generates synthetic variables using the **entire dataset** *before* `train_test_split` is called.
- **Why it affects the paper:** This violates strict machine learning pipeline hygiene. The training set "sees" the statistical distribution of the test set, leading to data leakage. This artificially inflates model performance metrics and recourse benchmark stability, which reviewers at FAccT will immediately flag as a critical methodological flaw.

### B. Severe Bureau Artefact Distortion (FICO Negative Values)
- **Files Affected:** `src/data_loader.py` (Line: `110` for HELOC)
- **The Issue:** The FICO dataset encodes special statuses as negative integers (e.g., `-7` = Condition not met, `-8` = No usable trades). The data loader currently converts all negative values to `0.0` blindly (`lambda v: 0.0 if v < 0 else float(v)`).
- **Why it affects the paper:** This destroys the semantic meaning of the data. For instance, `MSinceMostRecentInqexcl7days` = `-7` (no inquiries) gets mapped to `0.0` (zero months since last inquiry, implying extreme recent credit-seeking behavior). The model heavily penalizes safe borrowers because of this artifact. A paper reporting results on such distorted data will be rejected on the grounds of poor domain understanding and invalid empirical baselines.

---

## 2. Failing Unit Tests & Logic Bugs

A robust compliance framework must pass its own logical constraints. Currently, the Policy & Constraint Layer (PCL) is failing its core tests.

### A. Failing Monotonicity & Constraint Tests
- **Files Affected:** `tests/test_constraints.py` and `tests/test_policy_layer.py`
- **The Issue:** Running `pytest` results in 3 out of 4 tests failing:
  - `test_negative_savings_violation`: The PCL fails to catch when an applicant's savings decrease inappropriately.
  - `test_debt_increase_violation`: The PCL fails to catch when an applicant's revolving debt increases.
  - `test_valid_recourse`: A valid recourse plan is incorrectly flagged as a violation.
- **Why it affects the paper:** The PCL is the "deterministic referee" at the heart of your proposed system architecture. If the unit tests proving its correctness fail, the framework cannot be trusted to generate "Domain-Constrained" counterfactuals, rendering the core premise of the paper mathematically unsound.

---

## 3. Moderate Gaps

### A. Arbitrary Percentage-to-Dollar Conversion
- **Files Affected:** `src/cost_feasibility.py` (Lines: `21-24`)
- **The Issue:** The codebase arbitrarily maps a 1% drop in utilization to a flat $100 paydown cost, assuming every borrower has a uniform $10,000 credit limit.
- **Why it affects the paper:** A 10% drop on a $2,000 card ($200 cost) is fundamentally different from a 10% drop on a $50,000 HELOC ($5,000 cost). This invalidates the **Temporal Solvency (Execution Horizon)** calculations across different income brackets, which is a major contribution of the paper. This needs to be dynamically scaled based on inferred individual credit limits.

---

## Recommended Next Steps

1. **Fix the failing tests:** Resolve the logic in `src/policy_layer.py` so that it accurately enforces the `positive_metrics` and `adverse_metrics` lists, and correctly validates safe, positive monotonic changes.
2. **Refactor `src/data_loader.py`:** Move all statistical derivations (medians, imputations) *after* the train/test split. Use `NaN` mapping or distinct categorical bounds for FICO special variables instead of `0.0`.
3. **Fix `src/cost_feasibility.py`:** Use absolute dollar mappings derived from individual limits instead of a flat constant rate for percentage features.
4. **Fix Dependencies:** The `lightgbm` package is missing in the global scope; make sure all `requirements.txt` packages are correctly installed in the virtual environment.

Please click **Proceed** if you would like me to automatically patch these vulnerabilities and fix the failing tests.
