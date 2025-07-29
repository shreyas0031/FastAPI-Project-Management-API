from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    username: str
    password: str
    role: str
    full_name: str
    email: EmailStr
    mobile_number: str

class UserLogin(BaseModel):
    username: str
    password: str

class UserRead(BaseModel):
    id: int
    username: str
    role: str
    full_name: str
    email: EmailStr
    mobile_number: str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
