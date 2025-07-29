from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlmodel import Session
from typing import List

from app.core.config import settings
from app.schemas.project import ProjectCreate, ProjectRead
from app.models.project import Project
from app.services.project import get_projects, create_project, update_project, delete_project
from app.db.session import get_session

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username: str = payload.get("sub")
        role: str = payload.get("role")
        if username is None or role is None:
            raise credentials_exception
        return {"username": username, "role": role}
    except JWTError:
        raise credentials_exception

@router.get("/projects", response_model=List[ProjectRead])
def read_projects(session: Session = Depends(get_session), current_user: dict = Depends(get_current_user)):
    return get_projects(session)

@router.post("/projects", response_model=ProjectRead)
def create_new_project(project: ProjectCreate, session: Session = Depends(get_session), current_user: dict = Depends(get_current_user)):
    if current_user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Not authorized")
    db_project = Project(**project.dict())
    return create_project(session, db_project)

@router.put("/projects/{project_id}", response_model=ProjectRead)
def update_existing_project(project_id: int, project: ProjectCreate, session: Session = Depends(get_session), current_user: dict = Depends(get_current_user)):
    if current_user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Not authorized")
    db_project = update_project(session, project_id, project)
    if not db_project:
        raise HTTPException(status_code=404, detail="Project not found")
    return db_project

@router.delete("/projects/{project_id}")
def delete_existing_project(project_id: int, session: Session = Depends(get_session), current_user: dict = Depends(get_current_user)):
    if current_user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Not authorized")
    success = delete_project(session, project_id)
    if not success:
        raise HTTPException(status_code=404, detail="Project not found")
    return {"detail": "Project deleted successfully"}
