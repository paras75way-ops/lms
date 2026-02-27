from pydantic import BaseModel, EmailStr
from typing import Optional



class LoginRequest(BaseModel):
    username :str
    password: str

class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"

class RefreshTokenRequest(BaseModel):
    refresh_token: str

class TokenPayload(BaseModel):
    sub: str                
    role: str               
    exp: Optional[int] = None
    type: str                