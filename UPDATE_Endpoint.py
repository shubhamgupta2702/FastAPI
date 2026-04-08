from fastapi import FastAPI, Path, HTTPException, Query
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal
from fastapi.responses import JSONResponse
import json 


app = FastAPI()

class Patient(BaseModel):
  
  id:Annotated[str, Field(..., description="ID of the Patient", examples=["P001"])]
  name:Annotated[str, Field(..., description="Name of the Patient")]
  city:Annotated[str, Field(..., description="City of the Patient")]
  age:Annotated[int, Field(..., description="Age of the Patient", gt=0, lt=130)]
  gender:Annotated[Literal['male', 'female', 'other'], Field(..., description="Gender of the Patient", examples=['male', 'female','other'])]
  height:Annotated[float, Field(..., description="Height of the Patient in mtrs", gt=0)]
  weight:Annotated[float, Field(..., description="Weight of the Patient kgs", gt=0)]
  
  @computed_field
  @property
  def bmi(self) -> float:
    bmi = (self.weight)/(self.height**2)
    return bmi
  
  @computed_field
  @property
  def verdict(self) -> str:
    if self.bmi < 18.5:
      return "Underweight"
    elif self.bmi >19 and self.bmi <= 23:
      return "Normal"
    else:
      return "Obese"
  
def load_data():
  with open("patient.json") as f:
    data = json.load(f)
  return data

def save_data(data):
  with open('patient.json', 'w') as f:
    json.dump(data, f)
  
  
@app.post('/create')
def create_patient(patient:Patient):
  data = load_data()
  
  if patient.id in data:
    raise HTTPException(status_code=400, detail="patient already exists.")
  
  data[patient.id] = patient.model_dump(exclude=['id'])
  
  save_data(data=data)
  
  return JSONResponse(status_code=201, content={"message":"Patient created Successfully."})

@app.delete('/delete/{patient_id}')
def delete_patient(patient_id:str):
  data = load_data()
  
  if patient_id not in data:
    raise HTTPException(status_code=400, detail="Patient not found.")
  
  del data[patient_id]
  
  save_data(data=data)
  
  return JSONResponse(status_code=200, content={"message":"Patient deleted sucessfully"})

@app.put("/update/{patient_id}")
def update_patient(patient_id:str, patient_update:Patient):
  data = load_data()
  
  if patient_id not in data:
    raise HTTPException(status_code=400, detail="Patient not Found")
  
  existing_patient_info = data[patient_id]
  
  #existing_patient_info -> pydantic object -> update bmi + update verdict
  updated_patient_info = patient_update.model_dump(exclude_unset=True)
  
  for key, value in updated_patient_info.items():
    existing_patient_info[key] = value
    
  existing_patient_info['id'] = patient_id
  
  #pydantic object -> dictionary
  patient_pydantic_object = Patient(**existing_patient_info)
  
  existing_patient_info = patient_pydantic_object.model_dump(exclude='id')
  
  #add this dict to data
  data[patient_id] = existing_patient_info
  #save data
  save_data(data=data)
  return JSONResponse(status_code=200, content={"message":"Patient updated successfully."})