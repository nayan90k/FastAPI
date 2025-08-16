from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict


class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float #kg
    height: float #meters
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round((self.weight/(self.height**2)), 2)
        return bmi

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("inserted")

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print('BMI:', patient.bmi)
    print("updated")

patient_info = {"name": "kamalnayan", 'email': 'abc@hdfc.com',"age": '90', 'weight': 75.2, 'height':1.75, 'married':False, 'allergies':['pollen','dust'], 'contact_details': {'phone':'6278346237', 'emergency': '45634342'}}

patient1 = Patient(**patient_info) # validation -> type coercion

update_patient_data(patient1)
