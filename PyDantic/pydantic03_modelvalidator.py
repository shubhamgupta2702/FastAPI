from pydantic import BaseModel, Field, model_validator, EmailStr
from typing import Annotated, Optional, List, Dict

class Patient(BaseModel):
  name:str
  email:EmailStr
  age:int
  contact:Dict[str, int]
  
  
  @model_validator(mode='after')
  def emergency_contact_validator(model):
    if model.age > 55 and "emergency" not in model.contact:
      raise ValueError("neeed an emergency contact for the person whose age is gt 55")
    return model
  
  
def insert_into_DB(patient:Patient):
  print(patient.name)
  print(patient.age)
  print(patient.email)
  print(patient.contact)
  
  
patient_data = {"name":"Shubham gupta", "email":"shubh@hdfc.com", "age":65,"contact":{"Home":32435465,"emergency":463436473}}

patient1 = Patient(**patient_data)

insert_into_DB(patient=patient1)
