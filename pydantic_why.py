from pydantic import BaseModel
from typing import List, Dict, Optional

class Patient(BaseModel):
    name: str
    age: int
    weight: float
    married: bool = False
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]


def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("inserted")

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print("updated")

patient_info = {"name": "kamalnayan", "age": '30', 'weight': 75.2, 'contact_details': {'email': 'abc@gmail.com', 'phone':'6278346237'}}

patient1 = Patient(**patient_info)

update_patient_data(patient1)
