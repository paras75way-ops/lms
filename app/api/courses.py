from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.db.session import get_session

from app.repositories.course import CourseRepository
from app.repositories.user import UserRepository
from app.services.course import CourseService
from app.schemas.course import CourseCreateRequest, CourseCreate, CourseRead
from app.api.deps import get_current_instructor, get_current_user
from app.models.user import User

router = APIRouter(prefix="/courses", tags=["Courses"])


def get_course_service(session: Session = Depends(get_session)):
    return CourseService(CourseRepository(session), UserRepository(session))



@router.post("/", response_model=CourseRead, status_code=201)
def create_course(
    course_data: CourseCreateRequest,
    service: CourseService = Depends(get_course_service),
    current_user: User = Depends(get_current_instructor),
):
    """it is for creating course only instructor can create it"""
    internal = CourseCreate(
        title=course_data.title,
        description=course_data.description,
        instructor_id=current_user.id,   
    )
    return service.create_course(internal)


# i make it public so anyone can access it
@router.get("/", response_model=list[CourseRead])
def list_courses(service: CourseService = Depends(get_course_service)):
    return service.course_repo.get_all()


@router.get("/{course_id}", response_model=CourseRead)
def get_course(course_id: int, service: CourseService = Depends(get_course_service)):
    course = service.course_repo.get_by_id(course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course