from fastapi import FastAPI
from app.api import auth, project
from app.models.user import User
from app.models.project import Project
from app.db.session import engine

app = FastAPI()

@app.on_event("startup")
def on_startup():
    User.metadata.create_all(engine)
    Project.metadata.create_all(engine)

app.include_router(auth.router)
app.include_router(project.router)