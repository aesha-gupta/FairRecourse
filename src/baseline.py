import dice_ml
import pandas as pd


class UnconstrainedBaselineRecourse:
    """Baseline: Unconstrained standard DiCE that can vary all features without bounds."""
    def __init__(self, model, train_data: pd.DataFrame, continuous_features: list):
        df_dummy = train_data.copy()
        df_dummy["target"] = 0
        self.d = dice_ml.Data(dataframe=df_dummy, continuous_features=continuous_features, outcome_name="target")
        self.m = dice_ml.Model(model=model, backend="sklearn")
        self.exp = dice_ml.Dice(self.d, self.m, method="random")

    def generate(self, instance_df: pd.DataFrame, total_cfs: int = 3):
        dice_exp = self.exp.generate_counterfactuals(
            instance_df,
            total_CFs=total_cfs,
            desired_class=0,
        )
        return dice_exp.cf_examples_list[0].final_cfs_df