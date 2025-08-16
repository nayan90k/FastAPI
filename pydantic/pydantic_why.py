from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: Annotated[str, Field(max_length=50, title='Name of the patient', description='Give the name of patient in less than 50 chars', examples=['kamalnayan', 'kumar'])]
    email: EmailStr
    linkedin_url: AnyUrl
    age: int = Field(gt=0, lt=120)
    weight: Annotated[float, Field(gt=0, strict=True)]
    married: Annotated[bool, Field(default=False, description='Is the patient married or not?')]
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)]
    contact_details: Dict[str, str]


def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("inserted")

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print("updated")

patient_info = {"name": "kamalnayan", 'email': 'abc@gmail.com', 'linkedin_url':'http://linkedin.com/2323',"age": '30', 'weight': 75.2, 'contact_details': {'phone':'6278346237'}}

patient1 = Patient(**patient_info)

update_patient_data(patient1)
