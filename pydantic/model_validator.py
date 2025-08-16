from pydantic import BaseModel, EmailStr, model_validator
from typing import List, Dict


class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @model_validator(mode="after")
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError('Patients older than 60 must have an emergency contacts')
        return model
def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("inserted")

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print("updated")

patient_info = {"name": "kamalnayan", 'email': 'abc@hdfc.com',"age": '90', 'weight': 75.2, 'married':False, 'allergies':['pollen','dust'], 'contact_details': {'phone':'6278346237', 'emergency': '45634342'}}

patient1 = Patient(**patient_info) # validation -> type coercion

update_patient_data(patient1)
