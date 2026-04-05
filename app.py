from flask import Flask, request, jsonify
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

# ----------------------------
# Load model and column names
# ----------------------------
model = joblib.load("model.pkl")
columns = joblib.load("columns.pkl")  # make sure you saved this during training

# ----------------------------
# Home route
# ----------------------------
@app.route("/")
def home():
    return "Churn Prediction API is running"

# ----------------------------
# Prediction route
# ----------------------------
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get input data
        data = request.json["data"]

        # Convert to DataFrame with correct column names
        df = pd.DataFrame(data, columns=columns)

        # Make prediction
        prediction = model.predict(df)

        return jsonify({
            "prediction": int(prediction[0])
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        })

# ----------------------------
# Run app
# ----------------------------
if __name__ == "__main__":
    app.run(debug=True)