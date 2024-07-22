import json
import requests


url = 'https://fa41-182-69-88-45.ngrok-free.app/loan_prediction'

input_data = {
    "Gender": 1,
    "Married": 1,
    "Dependents": 1,
    "Education": 0,
    "Self_Employed": 0,
    "ApplicantIncome": 4583,
    "CoapplicantIncome": 0,
    "LoanAmount": 125,
    "Loan_Amount_Term": 360,
    "Credit_History": 1,
    "Property_Area": 2
}


input_data_json = json.dumps(input_data)
response = requests.post(url, data=input_data_json)
print(response.text)