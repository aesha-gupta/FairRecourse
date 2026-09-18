import numpy as np
import pandas as pd


class ModelMonitor:
    @staticmethod
    def calculate_psi(baseline: pd.Series, target: pd.Series, bins: int = 10) -> float:
        """
        Calculates the Population Stability Index (PSI) between two distributions.
        PSI < 0.10: Stable, 0.10 <= PSI < 0.25: Moderate Drift, PSI >= 0.25: Significant Drift.
        """
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
    def evaluate_recourse_stability(
        model,
        counterfactual_df: pd.DataFrame,
        original_instance: pd.DataFrame = None,
        threshold: float = 0.40,
        n_perturbations: int = 20,
        noise_level: float = 0.03,
    ) -> dict:
        """
        Evaluates epsilon-robustness: Tests whether the recourse plan survives execution
        wobble strictly on the actionable levers that changed.
        """
        # Isolate features that changed between original and counterfactual
        if original_instance is not None:
            active_cols = [
                col
                for col in counterfactual_df.select_dtypes(include=[np.number]).columns
                if col in original_instance.columns
                and abs(
                    float(counterfactual_df[col].iloc[0])
                    - float(original_instance[col].iloc[0])
                )
                > 1e-4
            ]
        else:
            active_cols = list(
                counterfactual_df.select_dtypes(include=[np.number]).columns
            )

        # If no actionable features changed, variance is 0
        if not active_cols:
            return {
                "stability_rate": 1.0,
                "is_stable": True,
                "perturbation_runs": n_perturbations,
            }

        # Vectorized batch perturbation (single inference pass)
        jittered_batch = pd.concat([counterfactual_df] * n_perturbations, ignore_index=True)
        for col in active_cols:
            val = float(counterfactual_df[col].iloc[0])
            noise = np.random.normal(0, noise_level * np.abs(val + 1e-5), size=n_perturbations)
            jittered_batch[col] = val + noise

        # Extract Probability of Default: column 1 for binary classification
        raw_probs = model.predict_proba(jittered_batch)
        pd_scores = raw_probs[:, 1] if raw_probs.ndim == 2 else raw_probs

        surviving_runs = int(np.sum(pd_scores < threshold))
        stability_rate = surviving_runs / n_perturbations

        return {
            "stability_rate": round(stability_rate, 3),
            "is_stable": stability_rate >= 0.85,
            "perturbation_runs": n_perturbations,
        }