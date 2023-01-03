# Import Necessary Libraries
import os
import json
import joblib

import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from pydantic import BaseModel

from fastapi import FastAPI, File, UploadFile

class Response(BaseModel):
    person_age: float
    person_income: float
    person_emp_length: float
    loan_amnt: float
    loan_int_rate: float
    loan_percent_income: float
    cb_person_cred_hist_length: float
    person_home_ownership_OTHER: float
    person_home_ownership_OWN: float
    person_home_ownership_RENT: float
    loan_intent_EDUCATION: float
    loan_intent_HOMEIMPROVEMENT: float
    loan_intent_MEDICAL: float
    loan_intent_PERSONAL: float
    loan_intent_VENTURE: float
    loan_grade_B: float
    loan_grade_C: float
    loan_grade_D: float
    loan_grade_E: float
    loan_grade_F: float
    loan_grade_G: float
    cb_person_default_on_file_Y: float

# File path
filepath = 'log_reg.pkl'

# Define a class for the credit model
class CreditModel:
  
  def load_model(self, filepath):
    """Loads the model"""
    self.model = joblib.load(filepath)

  async def predict(self, input_data):
    """does the prediction logic"""
    if not self.model:
      raise RuntimeError("Model is not loaded")
    print(type(input_data))  
    transformed_data = pd.DataFrame(
      input_data, index=[0]
    )
    prediction = self.model.predict(transformed_data)
    return prediction

app = FastAPI(title="Credit Worthiness API",debug=True)
credit_model = CreditModel()

@app.on_event("startup")
async def startup():
  """Loads model during start of the application"""
  credit_model.load_model(filepath)
  print(type(credit_model))

@app.post("/predict")
async def predict(json_object : Response):
  print(type(json_object.dict()))
  prediction = await credit_model.predict(json_object.dict())
  return {"prediction": prediction.tolist()}