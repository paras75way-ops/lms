from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.db.session import get_session
from app.repositories.user import UserRepository
from app.repositories.course import CourseRepository
from app.repositories.enrollment import EnrollmentRepository
from app.services.enrollment import EnrollementService
from app.api.deps import get_current_student
from app.models.user import User

router = APIRouter(prefix="/enrollment", tags=["Enrollment"])


def get_enrollement_service(session: Session = Depends(get_session)):
    return EnrollementService(
        UserRepository(session),
        CourseRepository(session),
        EnrollmentRepository(session)
    )


@router.post("/{course_id}")
def enroll(
    course_id: int,
    service: EnrollementService = Depends(get_enrollement_service),
    current_user: User = Depends(get_current_student),
):
    """agr student login h to wo course me enroll hoga"""
    return service.enroll_student(current_user.id, course_id)