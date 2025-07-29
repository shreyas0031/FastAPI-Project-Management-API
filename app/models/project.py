from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import date

class Project(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: str
    start_date: date
    end_date: date
    status: str  # e.g., "ongoing", "completed", "on-hold"
