🚀 Employee Attrition Prediction Backend (FastAPI + ML)
📌 Project Overview

This project is a machine learning–powered backend service for predicting employee attrition using Logistic Regression and Decision Tree models.

The backend is built with FastAPI and exposes REST APIs that allow a frontend application to submit employee details and receive attrition predictions in real time.

This project fulfills the requirements of an end-to-end ML pipeline, including:

Data preprocessing

Model training & evaluation

Model serialization using joblib

API integration

Deployment-ready backend

🧠 Machine Learning Models

The following models are used:

Logistic Regression

Decision Tree Classifier

Both models were trained using a cleaned and preprocessed employee dataset, including:

Missing value handling

Feature encoding

Feature scaling

Model evaluation

The trained models are exported using joblib and loaded dynamically by the API.

🏗️ Project Structure
employee-attrition-backend/
│
├── app/
│   ├── api.py              # FastAPI routes
│   ├── predict.py          # Prediction logic
│   ├── schemas.py          # Request/response schemas
│   └── __init__.py
│
├── models/
│   ├── logistic_model.joblib
│   └── decision_tree_model.joblib
│
├── requirements.txt
├── README.md
⚙️ Tech Stack

Backend Framework: FastAPI

ML Libraries: scikit-learn, pandas, numpy

Model Persistence: joblib

API Server: Uvicorn

Deployment: Render

🔌 API Endpoints
🔹 Logistic Regression Prediction

POST
/predict/logistic

🔹 Decision Tree Prediction

POST
/predict/decision-tree

🔹 API Documentation (Swagger)
/docs

▶️ Running the Project Locally
1️⃣ Clone the repository
git clone https://github.com/YOUR_USERNAME/employee-attrition-backend.git
cd employee-attrition-backend

2️⃣ Create & activate virtual environment
python -m venv venv
source venv/Scripts/activate   # Windows (Git Bash)

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Start the server
uvicorn app.api:app --reload

5️⃣ Open Swagger UI
http://127.0.0.1:8000/docs

🌐 Deployment

The backend is deployed using Render.

🔗 Live API Docs:

https://your-backend.onrender.com/docs

🧪 Model Training

The models were trained in a Google Colab notebook, which includes:

Data cleaning

Feature engineering

Model training

Evaluation

Exporting models with joblib

The trained models are stored in the models/ directory and loaded during runtime.

✔ End-to-end ML pipeline
✔ Logistic Regression & Decision Tree
✔ Model persistence using joblib
✔ FastAPI backend integration
✔ Swagger documentation
✔ Deployment-ready backend

👤 Author

Alpha Israel 
Machine Learning & Software Engineering Student
