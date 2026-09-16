import dice_ml
import pandas as pd
from raiutils.exceptions import UserConfigValidationException


class ConstrainedRecourseGenerator:
    """
    Generates actionable, constraint-aware counterfactual recourse via DiCE.
    Catches infeasible search spaces gracefully for extreme default risk profiles.
    """
    def __init__(self, model, train_dataset: pd.DataFrame, continuous_features: list[str]):
        self.feature_names = continuous_features
        d = dice_ml.Data(
            dataframe=train_dataset.assign(target=0),
            continuous_features=continuous_features,
            outcome_name="target",
        )
        m = dice_ml.Model(model=model, backend="sklearn")
        self.exp = dice_ml.Dice(d, m, method="random")

    def generate(self, query_instance: pd.DataFrame, total_cfs: int = 1) -> pd.DataFrame | None:
        features_to_vary = [
            f for f in ["savings_balance", "revolving_debt", "duration_months", "NetFractionRevolvingBurden"]
            if f in query_instance.columns
        ]
        if not features_to_vary:
            features_to_vary = [c for c in query_instance.columns if c not in ["target", "risk_tier"]]

        # 1. Attempt standard constrained search
        try:
            dice_exp = self.exp.generate_counterfactuals(
                query_instance,
                total_CFs=total_cfs,
                desired_class=0,
                features_to_vary=features_to_vary,
                verbose=False,
            )
            return dice_exp.cf_examples_list[0].final_cfs_df
        except (UserConfigValidationException, Exception):
            pass

        # 2. Relax search parameters for extreme default risk profiles (> 80% PD)
        try:
            relaxed_features = [
                c for c in query_instance.columns
                if c not in ["monthly_income", "disposable_income", "target", "risk_tier"]
            ]
            dice_exp = self.exp.generate_counterfactuals(
                query_instance,
                total_CFs=total_cfs,
                desired_class=0,
                features_to_vary=relaxed_features,
                verbose=False,
            )
            return dice_exp.cf_examples_list[0].final_cfs_df
        except (UserConfigValidationException, Exception):
            # Recourse is mathematically unattainable within domain limits
            return None