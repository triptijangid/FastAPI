from fastapi import FastAPI, Depends, Header, HTTPException
from pydantic import BaseModel, EmailStr, Field

app = FastAPI()

VALID_TOKENS = {
    "tok_abc123": "priya@masai.com",
    "tok_def456": "rahul@masai.com"
}

EXISTING_ENROLLMENTS = [
    {
        "email": "priya@masai.com", "course_id": "PY101"
    },
    {
        "email": "rahul@masai.com", "course_id": "SQL201"
    }
]

class EnrollmentRequest(BaseModel):
    email: EmailStr
    course_id: str = Field(max_length = 10)

def verify_token(token: str = 
                 Header(...)):
    if token not in VALID_TOKENS: 
        raise HTTPException(status_code=401, detail="Invalid Credentials")
    return VALID_TOKENS[token]

@app.post("/enroll")
def enroll(request: EnrollmentRequest, user_email: str = Depends(verify_token)):
    for enrollment in EXISTING_ENROLLMENTS:
        if (enrollment["email"] == request.email and enrollment["course_id"] == request.course_id):
            raise HTTPException(status_code=400, detail="Already Enrolled")
        return {"message": "Enrolled Successful", "email": request.email, "course_id": request.course_id}
    
# Token validation is implemented as a dependency using Depends so that it can be reused across multiple endpoints.