from sqlmodel import SQLModel, create_engine, Session
from app.core.config import settings

engine = create_engine(settings.DATABASE_URL, echo=True)

def get_session():
    with Session(engine) as session:
        yield session
