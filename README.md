# FairRecourse

An auditable machine learning recourse and governance framework that turns counterfactual explanations into realistic, feasible financial interventions.

## Core Highlights

*   **Calibrated Risk Engine:** LightGBM paired with isotonic calibration to ensure accurate default probability estimates.
*   **Explainability:** TreeSHAP attributions isolating key default drivers for adverse action compliance.
*   **Policy & Constraint Layer (PCL):** Enforces feature immutability (e.g., fixed income), monotonicity, and causal financial identities.
*   **Temporal Pacing:** Evaluates recourse plans against realistic monthly budgets and execution time horizons.
*   **Enterprise Monitoring:** Population Stability Index (PSI) drift tracking and $\epsilon$-stability perturbation audits.
*   **Dual Benchmarks:** Tested on Statlog German Credit ($1k$ rows) and FICO HELOC ($10k$ rows).

## Baseline vs. FairRecourse

Standard counterfactual search algorithms exploit optimization shortcuts (like telling an applicant to arbitrarily multiply their income) to cross decision boundaries:

| Audit Metric / Feature | Baseline (Standard DiCE) | FairRecourse (PCL Constrained) |
| :--- | :--- | :--- |
| **Deterministic Feasibility** | FAILED | PASSED |
| **Execution Horizon (Months)** | 1.0 mos | 22.4 mos |
| **Actionable Plan** | Income x7 (Impossible) | Pay down €208 debt, -2m tenure |
| **Violation Caught** | monthly_income mutated | Zero Policy Violations |

## Quickstart

Install dependencies:

pip install -r requirements.txt


Run side-by-side comparative audit:

python run_full_audit.py --dataset german
python run_full_audit.py --dataset heloc


Run population fairness & sensitivity audit:

python run_audit.py --dataset german
python run_audit.py --dataset heloc


Run test suite:
pytest tests/


## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
