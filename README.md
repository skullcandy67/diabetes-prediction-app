#  Diabetes Prediction Web App

A machine learning-powered web application built with Flask to predict the likelihood of diabetes based on user input. It uses SMOTE to handle class imbalance and leverages multiple ensemble models for robust and accurate predictions.

---

##  Features

- User-friendly web interface for input & prediction
- Data preprocessing pipeline:
  - KNN Imputation
  - Ordinal Encoding
- Class imbalance handled with **SMOTE**
- Ensemble models:
  -  Voting Classifier (Hard & Soft)
  -  Stacking Classifier (**Best Performer**)
  -  CalibratedClassifierCV for probability calibration
- Dockerized for seamless deployment

---

##  Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS (Bootstrap)
- **ML Libraries**: scikit-learn, imbalanced-learn, LightGBM, CatBoost
- **Deployment**: Docker, Render

---

##  Live Demo

👉 [Diabetes Predictor on Render](https://diabetes-prediction-app-1-8gwa.onrender.com)

---

##  Run Locally with Docker

```bash
git clone https://github.com/yourusername/diabetes-predictor.git
cd diabetes-predictor
docker build -t diabetes_pred .
docker run -p 8888:5000 diabetes_pred

