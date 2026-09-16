import warnings
import shap
import pandas as pd
import numpy as np


class ExplainerEngine:
    def __init__(self, trained_model, background_data: pd.DataFrame):
        base_lgb = trained_model.calibrated_model.calibrated_classifiers_[0].estimator
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            self.explainer = shap.TreeExplainer(base_lgb)
        self.feature_names = list(background_data.columns)

    def explain_instance(self, instance_df: pd.DataFrame, top_k: int = 3):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            shap_values = self.explainer.shap_values(instance_df)

        if isinstance(shap_values, list):
            sv = shap_values[1][0]
        elif len(shap_values.shape) == 3:
            sv = shap_values[0, :, 1]
        else:
            sv = shap_values[0]

        contributions = []
        for name, val, s in zip(self.feature_names, instance_df.iloc[0], sv):
            contributions.append({
                "feature": name,
                "current_value": val,
                "shap_value": round(float(s), 4),
                "risk_direction": "Increases Default Risk" if s > 0 else "Decreases Default Risk"
            })

        df_contrib = pd.DataFrame(contributions)
        df_sorted = df_contrib.sort_values(by="shap_value", ascending=False).reset_index(drop=True)
        return df_sorted.head(top_k)