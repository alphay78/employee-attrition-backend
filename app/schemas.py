from pydantic import BaseModel

class EmployeeFeatures(BaseModel):
    age: int
    monthly_income: float
    job_level: int
    job_satisfaction: int
    years_at_company: int
    overtime: str
    department: str
    education_field: str
