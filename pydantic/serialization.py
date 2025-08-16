from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    pin: str

class Patient(BaseModel):
    name: str
    gender: str = 'Male'
    age: int
    address: Address

address_dict={'city':'buxar', 'state':'bihar', 'pin': '802123'}

address1 = Address(**address_dict)

patient_dict={'name': 'kamalnayan', 'age': 23, 'address': address1}

patient1 = Patient(**patient_dict)

temp = patient1.model_dump()

print(temp)
print(type(temp))

temp_2 = patient1.model_dump_json()
print(temp_2)
print(type(temp_2))


temp_3= patient1.model_dump(exclude={'address':['state']}) # include, exclude

print(temp_3)
print(type(temp_3))

temp_4= patient1.model_dump(exclude_unset=True)

print(temp_4)
print(type(temp_4))