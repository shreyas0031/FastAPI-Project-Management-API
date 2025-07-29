from sqlmodel import Session, select
from app.models.project import Project

def get_projects(session: Session):
    return session.exec(select(Project)).all()

def create_project(session: Session, project_data: Project) -> Project:
    session.add(project_data)
    session.commit()
    session.refresh(project_data)
    return project_data

def update_project(session: Session, project_id: int, project_data: Project) -> Project:
    db_project = session.get(Project, project_id)
    if not db_project:
        return None
    for key, value in project_data.dict().items():
        setattr(db_project, key, value)
    session.commit()
    session.refresh(db_project)
    return db_project

def delete_project(session: Session, project_id: int) -> bool:
    db_project = session.get(Project, project_id)
    if not db_project:
        return False
    session.delete(db_project)
    session.commit()
    return True
