import numpy as np
import pandas as pd


class ModelMonitor:
    @staticmethod
    def calculate_psi(baseline: pd.Series, target: pd.Series, bins: int = 10) -> float:
        """
        Calculates the Population Stability Index (PSI) between two distributions.
        PSI < 0.10: Stable, 0.10 <= PSI < 0.25: Moderate Drift, PSI >= 0.25: Significant Drift.
        """
        # Determine quantile bins based on baseline
        quantiles = np.linspace(0, 1, bins + 1)
        bin_edges = np.percentile(baseline.dropna(), quantiles * 100)
        bin_edges[0] -= 1e-5
        bin_edges[-1] += 1e-5

        base_counts = np.histogram(baseline.dropna(), bins=bin_edges)[0]
        target_counts = np.histogram(target.dropna(), bins=bin_edges)[0]

        # Normalize with Laplace smoothing to avoid division by zero
        base_pct = (base_counts + 1e-4) / (len(baseline) + 1e-4 * bins)
        target_pct = (target_counts + 1e-4) / (len(target) + 1e-4 * bins)

        psi_val = np.sum((target_pct - base_pct) * np.log(target_pct / base_pct))
        return round(float(psi_val), 4)

    @staticmethod
    def evaluate_recourse_stability(model, counterfactual_df: pd.DataFrame, threshold: float = 0.40, n_perturbations: int = 20, noise_level: float = 0.03) -> dict:
        """
        Evaluates epsilon-robustness: Does the recourse profile remain approved if
        the applicant slightly under-fulfills the target or model scores jitter by +/- delta?
        """
        numeric_cols = counterfactual_df.select_dtypes(include=[np.number]).columns
        surviving_runs = 0

        for _ in range(n_perturbations):
            jittered_df = counterfactual_df.copy()
            for col in numeric_cols:
                # Inject mild Gaussian noise representing execution discrepancy
                noise = np.random.normal(0, noise_level * np.abs(jittered_df[col].values[0] + 1e-5))
                jittered_df[col] = jittered_df[col] + noise

            pred_prob = model.predict_proba(jittered_df)[0]
            if pred_prob < threshold:
                surviving_runs += 1

        stability_rate = surviving_runs / n_perturbations
        return {
            "stability_rate": round(stability_rate, 3),
            "is_stable": stability_rate >= 0.85,
            "perturbation_runs": n_perturbations
        }