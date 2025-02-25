from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import pickle
import pandas as pd

app = FastAPI()

# Load the trained model
with open("models/model.pkl", "rb") as f:
    model = pickle.load(f)

# Load Templates
templates = Jinja2Templates(directory="templates")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict/")
def predict(data: dict):
    try:
        # Convert data to DataFrame
        df = pd.DataFrame([data])

        # Ensure feature alignment
        feature_order = [
            "age", "length_of_stay", "previous_admissions",
            "admission_type_emergency", "admission_type_routine", "admission_type_urgent",
            "diagnosis_asthma", "diagnosis_diabetes", "diagnosis_hypertension",
            "medications_albuterol", "medications_insulin", "medications_metformin"
        ]
        
        # One-hot encoding
        df = pd.get_dummies(df, columns=["admission_type", "diagnosis", "medications"])
        
        # Ensure all features are present
        for col in feature_order:
            if col not in df.columns:
                df[col] = 0  # Fill missing categories
        
        df = df[feature_order]  # Arrange columns correctly
        
        # Make Prediction
        prediction = model.predict(df)[0]
        
        return {"readmitted": bool(prediction)}

    except Exception as e:
        return {"error": str(e)}
