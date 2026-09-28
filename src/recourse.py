import numpy as np
import pandas as pd
import json
import os


class BufferedRiskModelWrapper:
    """Wraps a calibrated classifier with an operational safety buffer.
    
    Predicts Class 0 (Approval) strictly when Calibrated PD <= (Threshold - Buffer).
    """
    def __init__(self, base_model, operational_threshold: float = 0.40, safety_margin: float = 0.05):
        self.base_model = base_model
        self.target_threshold = operational_threshold - safety_margin
        self.classes_ = getattr(base_model, "classes_", np.array([0, 1]))

    def predict(self, x):
        raw_prob = self.base_model.predict_proba(x)
        pd_score = raw_prob[:, 1] if raw_prob.ndim == 2 else raw_prob
        return (pd_score > self.target_threshold).astype(int)

    def predict_proba(self, x):
        return self.base_model.predict_proba(x)


class ConstrainedRecourseGenerator:
    """Dataset-scoped recourse generator preventing cross-dataset contamination."""

    def __init__(
        self,
        model,
        train_dataset: pd.DataFrame,
        continuous_features: list[str],
        dataset_name: str = "heloc",
        operational_threshold: float = 0.40,
        safety_margin: float = 0.05,
        config_path: str = None,
        **kwargs,
    ):
        self.raw_model = model
        self.model = model
        self.feature_names = continuous_features
        self.dataset_name = dataset_name.lower()
        self.operational_threshold = operational_threshold

        if config_path is None:
            config_path = os.path.join(os.path.dirname(__file__), "..", "config", "default_schema.json")
            
        try:
            with open(config_path, 'r') as f:
                config = json.load(f)
            self.actionable_configs = config.get("ACTIONABLE_CONFIGS", {})
        except (FileNotFoundError, json.JSONDecodeError):
            self.actionable_configs = {}

        # Compute distributional MAD for scaling costs and normalized steps
        numeric_cols = list(train_dataset.select_dtypes(include=[np.number]).columns)
        medians = train_dataset[numeric_cols].median()
        self.mads = (train_dataset[numeric_cols] - medians).abs().median()
        self.mads = self.mads.replace(0.0, 1.0)

        # Set actionable levers based on dataset config
        cfg = self.actionable_configs.get(self.dataset_name, {})
        self.actionable_features = [f for f in cfg.keys() if f in self.feature_names]
        self.allowed_levers = self.actionable_features

    def _get_search_axis(self, feature: str, cur_val: float, steps: int = 5) -> np.ndarray:
        cfg = self.actionable_configs.get(self.dataset_name, {}).get(feature, {})
        direction = cfg.get("direction", "decrease")
        step = cfg.get("step", 5.0)

        if direction == "decrease":
            min_val = cfg.get("min", 0.0)
            grid = np.arange(cur_val, min_val - 1e-5, -step)
        else:
            max_val = cur_val + cfg.get("max_add", 2500.0)
            grid = np.arange(cur_val, max_val + 1e-5, step)

        if len(grid) == 0:
            grid = np.array([cur_val])
        return np.unique(np.round(grid, 4))

    def generate(
        self,
        query_instance: pd.DataFrame,
        pcl=None,
        evaluator=None,
        total_cfs: int = 1,
        max_active_levers: int = 2,
        grid_resolution: int = 5,
        max_horizon_months: float = 24.0,
        allowed_features: list[str] | None = None,  # <-- 1. Added parameter
        **kwargs,
    ) -> pd.DataFrame | None:
        base_series = query_instance.iloc[0]
        active_candidates = [
            f for f in self.actionable_features if f in query_instance.columns
        ]

        # <-- 2. Added filter: restricts search space if a pathway is specified
        if allowed_features is not None:
            active_candidates = [f for f in active_candidates if f in allowed_features]

        if not active_candidates:
            return None

        active_levers = active_candidates[:max_active_levers]
        feature_axes = [
            self._get_search_axis(feat, float(base_series[feat]), steps=grid_resolution)
            for feat in active_levers
        ]
        mesh = np.array(np.meshgrid(*feature_axes)).T.reshape(-1, len(active_levers))

        valid_plans = []
        min_pd_seen = 1.0

        for point in mesh:
            cand_series = base_series.copy()
            for idx, feat in enumerate(active_levers):
                cand_series[feat] = float(point[idx])

            # 1. PCL Constraint Check
            is_valid, violations = pcl.validate(base_series, cand_series) if pcl else (True, [])
            if not is_valid:
                continue

            # 2. In-Loop Temporal Horizon & Feasibility Check (matched signature)
            if evaluator:
                eval_metrics = evaluator.evaluate(base_series, cand_series, violations)
                if not eval_metrics.get("feasible", True):
                    continue
                # Both key variations checked safely
                months = eval_metrics.get("months_required", eval_metrics.get("execution_horizon_months", 0.0))
                if months > max_horizon_months:
                    continue

            cand_df = pd.DataFrame([cand_series])[query_instance.columns]

            # 3. Vectorized Stability Check (20 runs under 3% execution noise)
            batch = pd.concat([cand_df] * 20, ignore_index=True)
            for idx, feat in enumerate(active_levers):
                val = float(point[idx])
                if val != 0.0:
                    batch[feat] += np.random.normal(0, 0.03 * abs(val), size=20)

            probs = self.raw_model.predict_proba(batch)
            pd_scores = probs[:, 1] if probs.ndim == 2 else probs

            base_pd = float(pd_scores[0])
            if base_pd < min_pd_seen:
                min_pd_seen = base_pd

            stability_rate = float(np.mean(pd_scores < self.operational_threshold))

            if stability_rate >= 0.85:
                normalized_cost = sum(
                    abs(point[i] - float(base_series[active_levers[i]]))
                    / float(self.mads.get(active_levers[i], 1.0))
                    for i in range(len(active_levers))
                )
                valid_plans.append((normalized_cost, stability_rate, cand_df))

        if valid_plans:
            valid_plans.sort(key=lambda x: x[0])
            return valid_plans[0][2]

        print(f"Lowest PD reached by solver: {min_pd_seen:.4f}")
        return None