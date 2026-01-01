from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import EmployeeFeatures
from app.predict import predict_logistic, predict_decision_tree

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins (OK for dev)
    allow_credentials=True,
    allow_methods=["*"],  # allow POST, OPTIONS, etc.
    allow_headers=["*"],
)

@app.post("/predict/logistic")
def logistic_prediction(features: EmployeeFeatures):
    return predict_logistic(features)


@app.post("/predict/decision-tree")
def decision_tree_prediction(features: EmployeeFeatures):
    return predict_decision_tree(features)
