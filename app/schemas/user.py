from pydantic import BaseModel, EmailStr
from app.models.user import UserRole

class UserCreate(BaseModel):
    full_name: str
    email: EmailStr
    password: str 
    role: UserRole

class UserRead(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    role: UserRole
    
    class Config:
        from_attributes = True