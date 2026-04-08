from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
  name: Annotated[str, Field(max_length=50, description="The name o the patient less than 50 words", examples=["Shubham", "Angel"], title="name of patient")]
  age:int
  married:bool = False
  weight:Annotated[Optional[float], Field(gt=0, description="Weight og the Patient in kg.", default=None, strict=True)]
  height:float
  allergies: Optional[List[str]] = None
  hobbies: Dict[str, List[str]]
  email:Annotated[EmailStr, Field(title="Email/Gmail", description="Email/Gmail of the Patient", examples="abc@gmail.com")]
  portfolio_url:Annotated[AnyUrl, Field(description="The url of patient portfolio for their medical records", examples="https://shubhamg.vercel.com")]
  
def insert_patient_data(patient: Patient):
  print(patient.name)
  print(patient.age)
  print(patient.hobbies)
  print(patient.height)
  print(patient.weight)
  print(patient.allergies)
  print(patient.married)
  print(patient.email)
  print(patient.portfolio_url)
  print("Data Inserted into DB")
  
patient_info = {"name":"shubham", "age":"31", "married": True, "weight":56.7, "height":171, "hobbies":{"physical_game":["Cricket", "Football", "VolleyBall"], "mobile_games":["Free Fire", "BGMI Esports"]}, "allergies":["Mint", "GrainDust"], "email":"shubh@gmail.com", "portfolio_url":"https://shubham2702.com"}  
#pydantic is smart enough to parse string into integer

patient2_info = {"name":"shubham", "age":"31", "weight":56.7, "height":171, "hobbies":{"physical_game":["Cricket", "Football", "VolleyBall"], "mobile_games":["Free Fire", "BGMI Esports"]}, "email":"abs23@gmail.com", "portfolio_url":"https://absce463643.com"} 

patient1 = Patient(**patient_info)
patient2 = Patient(**patient2_info)

print("Patient1 - \n")
insert_patient_data(patient=patient1)
print("Patient2 - \n")
insert_patient_data(patient=patient2)