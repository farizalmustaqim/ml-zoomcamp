#!/usr/bin/env python
# coding: utf-8

import requests

url = 'http://localhost:8000/predict'

customer = {
    "gender": "female",
    "age": 50,
    "hypertension": 1,
    "heart_disease": 0,
    "ever_married": "no",
    "work_type": "Private",
    "Residence_type": "Urban",
    "avg_glucose_level": 300.0,
    "bmi": 20.0,
    "smoking_status": "smokes"
}
response = requests.post(url, json=customer).json()
print(response)

if response['stroke'] == True:
    print('patient has stroke')

else:
    print('patient does not have stroke')
