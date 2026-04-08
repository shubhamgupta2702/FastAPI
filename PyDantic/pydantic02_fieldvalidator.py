from pydantic import BaseModel, Field, field_validator, EmailStr
from typing import Annotated, Optional, List, Dict

class Patient(BaseModel):
  name:str
  email:EmailStr
  age:int
  contact:Dict[str, int]
  
  @field_validator('email')
  @classmethod
  def email_validator(cls, value):
    domains_available = ['hdfc.com', 'icici.com','axisbank.com', 'ubi.com']
    domain = value.split('@')[-1]
    
    if domain not in domains_available:
      raise ValueError("Not a valid email.")
    return value
  
  @field_validator('name')
  @classmethod
  def name_uppercase(cls, value):
    return value.upper()
  
  
def insert_into_DB(patient:Patient):
  print(patient.name)
  print(patient.age)
  print(patient.email)
  print(patient.contact)
patient_data = {"name":"Shubham gupta", "email":"shubh@hdfc.com", "age":32,"contact":{"Home":32435465,"emergency":463436473}}

patient1 = Patient(**patient_data)

insert_into_DB(patient=patient1)
