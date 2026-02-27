from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.db.session import get_session
from app.repositories.user import UserRepository
from app.services.user import UserService
from app.schemas.user import UserCreate, UserRead
from app.api.deps import get_current_user
from app.models.user import User

router = APIRouter(prefix="/users", tags=["Users"])


def get_user_service(session: Session = Depends(get_session)):
    return UserService(UserRepository(session))


#i made it public so anyon can access or register
@router.post("/", response_model=UserRead, status_code=201)
def register_user(user: UserCreate, service: UserService = Depends(get_user_service)):
    return service.register_user(user)


@router.get("/me", response_model=UserRead)
def get_me(current_user: User = Depends(get_current_user)):
    return current_user



 