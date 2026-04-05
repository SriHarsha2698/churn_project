import requests

url = "https://churn-api-sriharshapeetha-czcnbhbagad5gxfq.canadacentral-01.azurewebsites.net/predict"

data = {
    "data": [[
        0,      # SeniorCitizen
        12,     # tenure
        70.5,   # MonthlyCharges
        800,    # TotalCharges
        65,     # AvgCharges

        1,      # gender_Male
        1,      # Partner_Yes
        0,      # Dependents_Yes
        1,      # PhoneService_Yes
        0,      # MultipleLines_No phone service
        1,      # MultipleLines_Yes

        1,      # InternetService_Fiber optic
        0,      # InternetService_No

        0,      # OnlineSecurity_No internet service
        1,      # OnlineSecurity_Yes

        0,      # OnlineBackup_No internet service
        1,      # OnlineBackup_Yes

        0,      # DeviceProtection_No internet service
        1,      # DeviceProtection_Yes

        0,      # TechSupport_No internet service
        1,      # TechSupport_Yes

        0,      # StreamingTV_No internet service
        1,      # StreamingTV_Yes

        0,      # StreamingMovies_No internet service
        1,      # StreamingMovies_Yes

        0,      # Contract_One year
        1,      # Contract_Two year

        1,      # PaperlessBilling_Yes

        0,      # PaymentMethod_Credit card (automatic)
        1,      # PaymentMethod_Electronic check
        0       # PaymentMethod_Mailed check
    ]]
}

response = requests.post(url, json=data)

print(response.json())