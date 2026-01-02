import joblib
from pathlib import Path
from functools import lru_cache

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_DIR = BASE_DIR / "models"


@lru_cache()
def get_logistic_model():
    return joblib.load(MODEL_DIR / "logistic_model.joblib")


@lru_cache()
def get_decision_tree_model():
    return joblib.load(MODEL_DIR / "decision_tree_model.joblib")
