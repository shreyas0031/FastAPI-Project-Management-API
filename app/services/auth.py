from sqlmodel import Session, select
from fastapi import HTTPException
from app.models.user import User
from app.core.security import verify_password, get_password_hash

def authenticate_user(session: Session, username: str, password: str):
    user = session.exec(select(User).where(User.username == username)).first()
    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return user

def create_user(session: Session, username: str, password: str, role: str,
                full_name: str, email: str, mobile_number: str):
    hashed_password = get_password_hash(password)
    user = User(
        username=username,
        hashed_password=hashed_password,
        role=role,
        full_name=full_name,
        email=email,
        mobile_number=mobile_number
    )
    session.add(user)
    session.commit()
    session.refresh(user)
    return user
