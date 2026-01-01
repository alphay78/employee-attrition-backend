import joblib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_DIR = BASE_DIR / "models"

_logistic_model = None
_decision_tree_model = None


def get_logistic_model():
    global _logistic_model
    if _logistic_model is None:
        _logistic_model = joblib.load(
            MODEL_DIR / "logistic_model.joblib"
        )
    return _logistic_model


def get_decision_tree_model():
    global _decision_tree_model
    if _decision_tree_model is None:
        _decision_tree_model = joblib.load(
            MODEL_DIR / "decision_tree_model.joblib"
        )
    return _decision_tree_model
