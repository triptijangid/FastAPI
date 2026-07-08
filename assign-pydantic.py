from pydantic import BaseModel, Field, EmailStr, field_validator, model_validator, computed_field
from typing import Dict

class Learner(BaseModel):
    name: str = Field(max_length=40)          # TODO: add max_length constraint
    email: EmailStr
    age: int = Field(gt=15, lt=60)           # TODO: add gt and lt constraints
    course: str
    scores: Dict[str, float]

    @field_validator("email")
    @classmethod
    def validate_email_domain(cls, value):
        # TODO: extract domain and raise ValueError if not learnhub.com
        domain_name = value.split('@')[-1]

        if domain_name != 'learnhub.com':
            raise ValueError('The domain name is not valid')
        return value

    @field_validator("course")
    @classmethod
    def normalise_course(cls, value):
        # TODO: return value uppercased
        return value.upper()

    @model_validator(mode="after")
    def check_guardian_approval(self):
        # TODO: if age < 18 and "guardian_approved" not in scores, raise ValueError
        if self.age < 18 and self.scores.get("guardian_approved") != 1.0:
            raise ValueError('Learners under 18 must have "guardian_approved": 1.0 in scores.')
        return self

    @computed_field
    @property
    def average_score(self) -> float:
        # TODO: compute mean of scores excluding "guardian_approved"
        total = 0
        count = 0
        for subject, marks in self.scores.items():
            if subject != "guardian_approved":
                total += marks
                count +=1

        if count == 0:
            return 0.0
        
        return total / count


if __name__ == "__main__":
    learner_info_1 = {
        "name": "Jordan Lee",
        "email": "jordan@learnhub.com",
        "age": 22,
        "course": "data science",
        "scores": {"math": 85.0, "python": 90.0, "stats": 78.0}
    }
    learner = Learner(**learner_info_1)
    print(learner.course)          # Expected: DATA SCIENCE
    print(learner.average_score)   # Expected: ~84.33


    learner_info_2 = {
        "name": "Casey Patel",
        "email": "casey@learnhub.com",
        "age": 16,
        "course": "web dev",
        "scores": {"html": 70.0, "css": 65.0}
    }
    learner1 = Learner(**learner_info_2)
    print(learner1)