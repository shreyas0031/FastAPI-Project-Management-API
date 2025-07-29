from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.schemas.user import UserCreate, UserLogin, Token
from app.db.session import get_session
from app.services.auth import create_user, authenticate_user
from app.core.security import create_access_token

router = APIRouter()

@router.post("/register", response_model=Token)
def register(user: UserCreate, session: Session = Depends(get_session)):
    new_user = create_user(
        session,
        username=user.username,
        password=user.password,
        role=user.role,
        full_name=user.full_name,
        email=user.email,
        mobile_number=user.mobile_number
    )
    access_token = create_access_token({"sub": new_user.username, "role": new_user.role})
    return {"access_token": access_token}

@router.post("/login", response_model=Token)
def login(user: UserLogin, session: Session = Depends(get_session)):
    db_user = authenticate_user(session, user.username, user.password)
    access_token = create_access_token({"sub": db_user.username, "role": db_user.role})
    return {"access_token": access_token}
