from pydantic import BaseModel, EmailStr
from typing import Dict, List
class Student(BaseModel):
    name: str
    email: EmailStr
    age: int
    college: str
    marks: float
    emergency_number: Dict[str, int]

student_info = {'name' : 'Tripti', 'email' : 'triptijangid000@gmail.com', 'age' : '25', 'college': 'masai', 'marks': 35, 'emergency_number' : {'father' : 1233444444}}
student = Student(**student_info)
print(student)