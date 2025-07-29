from pydantic import BaseModel
from datetime import date

class ProjectCreate(BaseModel):
    name: str
    description: str
    start_date: date
    end_date: date
    status: str  # e.g., "ongoing", "completed", "on-hold"

class ProjectRead(ProjectCreate):
    id: int
