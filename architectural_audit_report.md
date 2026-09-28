# FairRecourse Architectural Audit Report

I have conducted a rigorous, line-by-line review of the `src/`, `config/`, and runner scripts against your six evaluation dimensions. The audit identified two critical data/mathematical vulnerabilities that threaten the validity of the experiments, one moderate mathematical gap, and several areas that received a clean bill of health.

---

## 1. Critical Vulnerabilities (Must Fix Immediately)

### A. Pre-Split Data Leakage (Target/Distribution Leak)
**File:** `src/data_loader.py`
**Lines:** `113-114` (HELOC) & `187` (CIBIL)
**Root Cause:** The scripts compute distributional statistics (`median_score = df[ext_col].median()`, `median_inc = X["monthly_income"].median()`) and generate synthetic variables using numpy random functions on the **entire dataset** *before* `train_test_split` is called.
**Impact:** This violates strict pipeline hygiene. The training set "sees" the statistical distribution of the test set, leading to data leakage that artificially inflates model performance metrics and benchmark stability.
**Remediation:** 
Compute medians and apply stochastic synthetic augmentation *after* splitting:
```python
X_train, X_test, ... = train_test_split(...)
median_score = X_train[ext_col].median()
# Apply transformations separately to X_train and X_test using the training statistics
```

### B. Severe Bureau Artefact Distortion (FICO Negative Values)
**File:** `src/data_loader.py`
**Line:** `110` (HELOC)
**Root Cause:** 
```python
df[col] = df[col].apply(lambda v: 0.0 if v < 0 else float(v))
```
**Impact:** The FICO dataset encodes special statuses as negative integers (e.g., `-7` = Condition not met, `-8` = No usable/valid trades, `-9` = No record). By blindly converting all negative values to `0.0`, the system destroys the semantic meaning of the data. For example, `MSinceMostRecentInqexcl7days` = `-7` (no inquiries) gets converted to `0.0` (zero months since last inquiry). The tree optimizer interprets this as extreme risk (hyper-recent credit seeking behavior), massively distorting the calibrated PD and penalizing safe borrowers.
**Remediation:**
Map FICO special values to `NaN` and use an imputer, or map them to logically consistent bounds (e.g., `-7` for months since inquiry should map to a very large number, like `999.0`, indicating infinite time since last inquiry).

---

## 2. Moderate Gaps & Inconsistencies

### A. Arbitrary Percentage-to-Dollar Conversion
**File:** `src/cost_feasibility.py`
**Lines:** `21-24`
**Root Cause:** 
```python
pct_drop = max(0.0, float(baseline.get(col, 0.0)) - float(candidate.get(col, 0.0)))
total_financial_shift += pct_drop * 100.0  # 1% drop = $100 paydown
```
**Impact:** Converting fractional burden/utilization metrics to a flat `$100 per 1%` assumes every borrower has a uniform $\$10,000$ limit. A borrower dropping utilization by 10% on a $\$2,000$ card pays $\$200$, while on a $\$50,000$ HELOC they pay $\$5,000$. This breaks the Temporal Solvency (Execution Horizon $H$) formula, making feasibility metrics incomparable across income brackets.
**Remediation:** Map utilization levers back to their absolute dollar debt features (e.g., `revolving_debt`) rather than applying a flat rate, or dynamically scale the conversion based on the applicant's derived limit.

---

## 3. Clean Bill of Health Sign-off

The following dimensions passed the stress test with exceptional architectural rigor:

### ✅ Model Calibration & Probability Estimation Rigor
- **`src/model.py`:** `CalibratedClassifierCV` (CV=3) is flawlessly configured. `predict_proba()` is used consistently, ensuring that the solver operates on true Platt/Isotonic probabilities rather than raw margins. 
- **Operational Thresholding:** The boundary of $\tau = 0.40$ is universally respected across `BufferedRiskModelWrapper`, `ModelMonitor`, and the audit runners.

### ✅ Recourse Optimizer & Constraint Enforcement
- **Scale-Invariant Formulation:** `compute_exposure_counter_offer` mathematically guarantees zero-division safety because it only executes if $PD > \tau$. The haircut cap enforces the economic viability bound flawlessly.
- **Search Grid & Step-Size Bounds:** `ConstrainedRecourseGenerator` in `src/recourse.py` dynamically honors `min` and `max_add` schema bounds, strictly obeying grid granularity.

### ✅ Policy & Constraint Layer (PCL) Verification
- **`src/policy_layer.py`:** Categorical mutations are safely caught via `try/except` float coercion blocks. Monotonicity string-matching correctly catches risk vs. quality invariants. Discrete counts are effectively protected from fractional generation with a `1e-3` float tolerance check (`abs(new_val - round(new_val)) > 1e-3`).

### ✅ Temporal Solvency & Epsilon-Stability 
- **`src/monitoring.py`:** The stochastic test rigorously applies Gaussian noise (`0.03 * abs(val)`) via a vectorized batch pass (`n_perturbations = 20`) strictly to the active levers without mutating the underlying immutable features. The `>= 0.85` threshold is securely enforced.
