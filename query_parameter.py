from fastapi import FastAPI, Path, HTTPException, Query
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

@app.get("/sort")
def sort_pateint(sort_by:str = Query(..., description="Sort on the basis of height, weight and bmi"), order:str = Query('asc', description="sort in asc or desc order")):
  
  valid_fields = ['height', 'weight', 'bmi']
  
  if sort_by not in valid_fields:
    raise HTTPException(status_code=400, detail=f'Invalid. Provide the values from {valid_fields}')
  
  if order not in ['asc','desc']:
    raise HTTPException(status_code=400, detail="Invalid. Please select asc or desc order")
  
  data = load_data()
  
  sort_order = True if order=='desc' else False
  
  sorted_data = sorted(data.values(), key= lambda x:x.get(sort_by,0), reverse=sort_order)
  
  return sorted_data