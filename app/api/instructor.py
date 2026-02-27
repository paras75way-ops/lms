from typing import List
from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.db.session import get_session

from app.repositories.course import CourseRepository
from app.repositories.enrollment import EnrollmentRepository
from app.repositories.module import ModuleRepository
from app.repositories.progress import ProgressRepository
from app.repositories.user import UserRepository
from app.services.instructor import InstructorService

from app.schemas.instructor import InstructorDashboardResponse, StudentProgressRead
from app.models.user import User
from app.api.deps import get_current_instructor

router = APIRouter(prefix="/instructor", tags=["Instructor Tools"])

def get_instructor_service(session: Session = Depends(get_session)):
    return InstructorService(
        CourseRepository(session),
        EnrollmentRepository(session),
        ModuleRepository(session),
        ProgressRepository(session),
        UserRepository(session)
    )
 
@router.get("/dashboard", response_model=InstructorDashboardResponse)
def get_my_dashboard(
    service: InstructorService = Depends(get_instructor_service),
    current_user: User = Depends(get_current_instructor)  
):
    return service.get_dashboard_analytics(instructor_id=current_user.id)


@router.get("/courses/{course_id}/students", response_model=List[StudentProgressRead])
def get_student_progress_list(
    course_id: int,
    service: InstructorService = Depends(get_instructor_service),
    current_user: User = Depends(get_current_instructor)  
):
    return service.get_course_student_progress(
        instructor_id=current_user.id, 
        course_id=course_id
    )