from app.schemas import EmployeeFeatures
import joblib
import pandas as pd
from functools import lru_cache


# =========================
# Load models (cached)
# =========================

@lru_cache()
def get_logistic_model():
    return joblib.load("models/logistic_model.joblib")


@lru_cache()
def get_decision_tree_model():
    return joblib.load("models/decision_tree_model.joblib")


# =========================
# DataFrame Builder
# =========================

def _build_dataframe(data: EmployeeFeatures) -> pd.DataFrame:
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
# Logistic Regression
# =========================

def predict_logistic(data: EmployeeFeatures):
    model = get_logistic_model()
    df = _build_dataframe(data)

    prediction = int(model.predict(df)[0])
    probability = float(model.predict_proba(df)[0][1])

    return {
        "attrition_prediction": prediction,
        "probability": round(probability, 4),
        "model_used": "logistic_regression"
    }


# =========================
# Decision Tree
# =========================

def predict_decision_tree(data: EmployeeFeatures):
    model = get_decision_tree_model()
    df = _build_dataframe(data)

    prediction = int(model.predict(df)[0])
    probability = float(model.predict_proba(df)[0][1])

    return {
        "attrition_prediction": prediction,
        "probability": round(probability, 4),
        "model_used": "decision_tree"
    }
