from typing import List
from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.db.session import get_session

from app.repositories.module import ModuleRepository
from app.repositories.progress import ProgressRepository
from app.services.learningservices import LearningService

from app.schemas.module import ModuleCreate, ModuleRead
from app.api.deps import get_current_instructor, get_current_user
from app.models.user import User

router = APIRouter(prefix="/modules", tags=["Modules"])


def get_learning_service(session: Session = Depends(get_session)):
    return LearningService(
        ModuleRepository(session),
        ProgressRepository(session)
    )


# only give access to instructr
@router.post("/", response_model=ModuleRead)
def create_module(
    module_in: ModuleCreate,
    service: LearningService = Depends(get_learning_service),
    current_user: User = Depends(get_current_instructor),
):
    return service.create_module(
        course_id=module_in.course_id,
        title=module_in.title,
        content_type=module_in.content_type,
        content_url=module_in.content_url,
    )



@router.get("/course/{course_id}", response_model=List[ModuleRead])
def get_course_modules(
    course_id: int,
    service: LearningService = Depends(get_learning_service),
    current_user: User = Depends(get_current_user),
):
    return service.module_repo.get_modules_by_course(course_id)