"""
LightGBM training and probability calibration (Platt/Isotonic)
"""
import lightgbm as lgb
from sklearn.calibration import CalibratedClassifierCV
from sklearn.metrics import brier_score_loss, precision_recall_curve, roc_auc_score, auc
import numpy as np


class CalibratedRiskModel:
    def __init__(self, random_state: int = 42):
        self.base_estimator = lgb.LGBMClassifier(
            n_estimators=100,
            learning_rate=0.05,
            max_depth=4,
            random_state=random_state,
            verbose=-1,
        )
        self.calibrated_model = CalibratedClassifierCV(
            estimator=self.base_estimator,
            method="sigmoid",
            cv=3,
        )
        self.fitted_ = False

    def fit(self, X, y):
        self.calibrated_model.fit(X, y)
        self.fitted_ = True
        return self

    def predict_proba(self, X):
        return self.calibrated_model.predict_proba(X)[:, 1]

    def predict(self, X, threshold: float = 0.40):
        return (self.predict_proba(X) >= threshold).astype(int)

    def evaluate(self, X, y):
        probs = self.predict_proba(X)
        roc = roc_auc_score(y, probs)
        precision, recall, _ = precision_recall_curve(y, probs)
        pr_auc = auc(recall, precision)
        brier = brier_score_loss(y, probs)
        return {"roc_auc": round(roc, 3), "pr_auc": round(pr_auc, 3), "brier_score": round(brier, 3)}