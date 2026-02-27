from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.db.session import get_session

from app.repositories.module import ModuleRepository
from app.repositories.progress import ProgressRepository
from app.services.learningservices import LearningService

from app.schemas.progress import ProgressRead, CourseProgressResponse
from app.api.deps import get_current_student
from app.models.user import User

router = APIRouter(prefix="/progress", tags=["Progress"])


def get_learning_service(session: Session = Depends(get_session)):
    return LearningService(
        ModuleRepository(session),
        ProgressRepository(session)
    )

@router.post("/{module_id}", response_model=ProgressRead)
def mark_module_complete(
    module_id: int,
    service: LearningService = Depends(get_learning_service),
    current_user: User = Depends(get_current_student),
):
     
    return service.mark_module_complete(current_user.id, module_id)



@router.get("/{module_id}/status")
def check_module_status(
    module_id: int,
    service: LearningService = Depends(get_learning_service),
    current_user: User = Depends(get_current_student),
):
    return service.check_module_status(current_user.id, module_id)


@router.get("/course/{course_id}", response_model=CourseProgressResponse)
def get_course_progress(
    course_id: int,
    service: LearningService = Depends(get_learning_service),
    current_user: User = Depends(get_current_student),
):
    return service.get_course_progress(current_user.id, course_id)