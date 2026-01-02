from app.schemas import EmployeeFeatures
import joblib
import pandas as pd
from functools import lru_cache
from fastapi import HTTPException


# =========================
# Load models (cached)
# =========================

@lru_cache()
def get_logistic_model():
    try:
        return joblib.load("models/logistic_model.joblib")
    except Exception as e:
        raise RuntimeError(f"Failed to load logistic model: {e}")


@lru_cache()
def get_decision_tree_model():
    try:
        return joblib.load("models/decision_tree_model.joblib")
    except Exception as e:
        raise RuntimeError(f"Failed to load decision tree model: {e}")


# =========================
# DataFrame Builder
# =========================

def _build_dataframe(data: EmployeeFeatures) -> pd.DataFrame:
    """
    Builds a single-row DataFrame matching the training feature set exactly.
    """
    return pd.DataFrame([{
        "Age": data.age,
        "MonthlyIncome": data.monthly_income,
        "JobLevel": data.job_level,
        "JobSatisfaction": data.job_satisfaction,
        "YearsAtCompany": data.years_at_company,
        "OverTime": data.overtime,
        "Department": data.department,
        "EducationField": data.education_field,
    }])


# =========================
# Helpers
# =========================

def _format_response(prediction: int, probability: float, model_name: str):
    # Ensure probability is always a valid float
    if probability is None or not isinstance(probability, (float, int)):
        probability = 0.0

    return {
        "attrition_prediction": prediction,
        "attrition": "Yes" if prediction == 1 else "No",
        "confidence": round(probability, 4),
        "model_used": model_name
    }


# =========================
# Logistic Regression
# =========================

def predict_logistic(data: EmployeeFeatures):
    try:
        model = get_logistic_model()
        df = _build_dataframe(data)

        prediction = int(model.predict(df)[0])
        probability = float(model.predict_proba(df)[0][1])

        return _format_response(
            prediction,
            probability,
            "logistic_regression"
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# =========================
# Decision Tree
# =========================

def predict_decision_tree(data: EmployeeFeatures):
    try:
        model = get_decision_tree_model()
        df = _build_dataframe(data)

        prediction = int(model.predict(df)[0])

        # Decision trees may or may not support predict_proba
        if hasattr(model, "predict_proba"):
            probability = float(model.predict_proba(df)[0][1])
        else:
            probability = 0.0

        return _format_response(
            prediction,
            probability,
            "decision_tree"
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
