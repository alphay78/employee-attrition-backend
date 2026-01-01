from pydantic import BaseModel

class EmployeeFeatures(BaseModel):
    Age: int
    MonthlyIncome: float
    JobLevel: int
    JobSatisfaction: int
    YearsAtCompany: int
    OverTime: str           # "Yes" / "No"
    Department: str
    EducationField: str
