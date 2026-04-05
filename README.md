# churn_project
End-to-end Customer Churn Prediction system with a Flask API, featuring data preprocessing, model training, and deployment-ready architecture.
# Customer Churn Prediction API

## 📌 Overview
This project is an end-to-end machine learning application designed to predict customer churn. It includes data preprocessing, feature engineering, model training, and deployment of a REST API using Flask.

The goal is to identify customers who are likely to leave a service, enabling businesses to take proactive retention measures.

---

## 🚀 Features
- Data preprocessing and cleaning
- Feature engineering (including AvgCharges)
- Class imbalance handling
- Model training and evaluation
- Comparison of multiple models (Logistic Regression, Random Forest, XGBoost)
- REST API built with Flask for real-time predictions

---

## 🧠 Model Performance
- Accuracy: ~76–79%
- Balanced precision and recall
- Optimized using hyperparameter tuning

---

## 🛠️ Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- XGBoost
- Flask
- Joblib

---

## 📡 API Usage

### Endpoint:
POST `/predict`

### Example Input:
```json
{
  "data": [[...]]
}
```
### Example Output:
```json
{
  "prediction": 1
}
