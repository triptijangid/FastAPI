from pydantic import BaseModel, EmailStr, Field, field_validator, model_validator
from typing import Dict, List
# By default all the parameters defined in Pydantic BaseModel are Mandatory
class Student(BaseModel):
    name: str = Field(max_length=50, description="Name")
    email: EmailStr
    age: int 
    college: str
    marks: float = Field(default=10.0)
    emergency_number: Dict[str, int]

    @field_validator('email')
    @classmethod
    def email_verification(cls, value):
        domain_name = value.split('@')[-1]

        if domain_name != 'masai.com':
            raise ValueError('Domain name is not valid.')
        return value
    
    @model_validator(mode='after')
    @classmethod
    def validate_contact_number(cls, model):
        if model.age < 18 and 'father' not in model.emergency_number:
            raise ValueError('If age is less than 18 then fathers contact number is mandatory.')
        return model

student_info = {'name' : 'Tripti', 'email' : 'triptijangid000@masai.com', 'age' : '16', 'college': 'masai', 'marks': 35, 'emergency_number' : {'father' : 1233444444}}
student = Student(**student_info)
print(student)