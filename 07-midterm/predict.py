from fastapi import FastAPI
import uvicorn
import pickle
import json
from pydantic import BaseModel

app = FastAPI()

model_file = 'random_forest.bin'

with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)

class CustomerData(BaseModel):
    gender: str
    age: int
    hypertension: int
    heart_disease: int
    ever_married: str
    work_type: str
    Residence_type: str
    avg_glucose_level: float
    bmi: float
    smoking_status: str

@app.get("/")
def home():
    return {"Hello": "World"}

@app.post("/predict")
async def predict(customer: CustomerData):
    customer_dict = customer.dict()
    X = dv.transform([customer_dict])
    y_pred = model.predict(X)
    stroke = y_pred >= 0.5

    result = {
        'stroke_probability': float(y_pred[0]),
        'stroke': bool(stroke[0])
    }

    return result
