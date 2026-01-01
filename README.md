🚀 Employee Attrition Prediction Backend

FastAPI · Machine Learning · REST API

📌 Project Overview

This project is a machine learning–powered backend service designed to predict employee attrition using supervised learning techniques.

The backend is built with FastAPI and exposes RESTful APIs that allow a frontend application to submit employee information and receive real-time attrition predictions using trained machine learning models.

The system implements a complete end-to-end machine learning pipeline, from data preprocessing and model training to deployment as a production-ready API.

🎯 Project Objectives

Build and evaluate Logistic Regression and Decision Tree models

Export trained models using joblib

Integrate models into a FastAPI backend

Expose prediction endpoints via REST APIs

Deploy the backend for public access

Provide interactive API documentation using Swagger UI

🧠 Machine Learning Models

The following models are implemented:

1️⃣ Logistic Regression

Used for baseline and interpretable predictions

Provides probability estimates for attrition

2️⃣ Decision Tree Classifier

Captures non-linear patterns in employee behavior

Used for comparative performance analysis

🧪 Data Preprocessing & Training

The models were trained on a cleaned and preprocessed employee dataset with the following steps:

Handling missing values

Encoding categorical features

Scaling numerical features

Model training and evaluation

Model comparison

Model serialization using joblib

The full training pipeline was implemented and executed in a Google Colab notebook.

🗂️ Project Structure
employee-attrition-backend/
│
├── app/
│   ├── api.py              # FastAPI route definitions
│   ├── predict.py          # Model loading & prediction logic
│   ├── schemas.py          # Pydantic request/response schemas
│   └── __init__.py
│
├── models/
│   ├── logistic_model.joblib
│   └── decision_tree_model.joblib
│
├── requirements.txt
├── README.md

⚙️ Technology Stack
Backend

FastAPI

Uvicorn

Machine Learning

scikit-learn

pandas

numpy

Model Persistence

joblib

Deployment

Render

🔌 API Endpoints
🔹 Logistic Regression Prediction

POST

/predict/logistic

🔹 Decision Tree Prediction

POST

/predict/decision-tree

🔹 Interactive API Documentation (Swagger)
/docs

▶️ Running the Project Locally
1️⃣ Clone the Repository
git clone https://github.com/YOUR_USERNAME/employee-attrition-backend.git
cd employee-attrition-backend

2️⃣ Create & Activate Virtual Environment
python -m venv venv
source venv/Scripts/activate   # Windows (Git Bash)

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Start the FastAPI Server
uvicorn app.api:app --reload

5️⃣ Open Swagger UI
http://127.0.0.1:8000/docs

🌐 Deployment

The backend is deployed using Render, making the API publicly accessible.

🔗 Live API Documentation:

https://your-backend.onrender.com/docs

📊 Assignment Requirements Coverage

✔ Complete end-to-end ML pipeline
✔ Logistic Regression & Decision Tree implementation
✔ Model evaluation and comparison
✔ Model persistence using joblib
✔ FastAPI backend integration
✔ RESTful prediction endpoints
✔ Swagger documentation
✔ Deployment-ready backend

👤 Author

Alpha Israel (Alphicho)
Machine Learning & Software Engineering Student
