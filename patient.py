from fastapi import FastAPI, Path, HTTPException
import json 


app = FastAPI()


def load_data():
  with open("patient.json") as f:
    data = json.load(f)
  return data
  
  
  
@app.get("/")
def title():
  return {"message":"Patient Management System"}

@app.get("/about")
def about():
  return {"message":"A fully functional pateint management system API"}

@app.get("/view")
def view():
  data = load_data()
  return data


@app.get("/patient/{patient_id}")
def get_patient(patient_id:str = Path(..., description="ID of the patient in DB", example="P001")):
  data = load_data()
  
  if patient_id in data:
    return data[patient_id]
  
  raise HTTPException(status_code=404, detail="Patient ID not Found.")