from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.db.session import get_session
from app.repositories.user import UserRepository
from app.services.authservice import AuthService
from app.schemas.auth import LoginRequest, RefreshTokenRequest

from fastapi.security import OAuth2PasswordRequestForm
router = APIRouter(prefix="/auth", tags=["Authentication"])



def get_auth_service(session: Session = Depends(get_session)):
    return AuthService(UserRepository(session))

@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    service: AuthService = Depends(get_auth_service),
):
    return service.authenticate_user(
        username=form_data.username,   
        password=form_data.password
    )


@router.post("/refresh")
def refresh_token(
    payload: RefreshTokenRequest,
    service: AuthService = Depends(get_auth_service),
):
    """used for getting new access token"""
    return service.refresh_access_token(payload.refresh_token)