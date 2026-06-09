from fastapi import FastAPI
import pandas as pd
import joblib

app = FastAPI()

model = joblib.load("stress_model.pkl")

@app.get("/")
def home():
    return {"message": "Student Stress Prediction API"}

@app.post("/predict")
def predict(data: dict):

    df = pd.DataFrame([data])

    prediction = int(model.predict(df)[0])
    probabilities = model.predict_proba(df)[0].tolist()

    return {
        "prediction": prediction,
        "probabilities": probabilities
    }