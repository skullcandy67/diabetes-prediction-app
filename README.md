#  Diabetes Prediction Web App

A machine learning web application built using Flask that predicts the likelihood of diabetes based on user input. It leverages SMOTE for handling class imbalance and uses multiple ensemble models for high accuracy.

---

##  Features

- User-friendly web interface
- Data preprocessing: KNN imputation + Ordinal Encoding
- Handles class imbalance using SMOTE
- Trained with:
  - Voting Classifier (hard & soft)
  - Stacking Classifier (best performer)
  - CalibratedClassifierCV for calibrated outputs
- Dockerized for deployment

---

##  Tech Stack

- Python, Flask, HTML/CSS
- scikit-learn, imbalanced-learn, LightGBM, CatBoost
- Docker

---

## 🔗 Live Demo

Check out the live deployed app: [Diabetes Predictor on Render](https://diabetes-prediction-app-1-8gwa.onrender.com)

---

## 🐳 Run Locally with Docker

```bash
git clone https://github.com/yourusername/diabetes-predictor.git
cd diabetes-predictor
docker build -t diabetes_pred .
docker run -p 8888:5000 diabetes_pred
