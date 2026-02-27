from fastapi import HTTPException
from app.models.user import UserRole
from app.models.course import Course
from app.schemas.course import CourseCreate

class CourseService:
    def __init__(self, course_repo, user_repo):
        self.course_repo = course_repo
        self.user_repo = user_repo

    def create_course(self, course_data: CourseCreate):
        instructor = self.user_repo.get_by_id(course_data.instructor_id)
        if not instructor or instructor.role != UserRole.INSTRUCTOR:
            raise HTTPException(status_code=400, detail="Invalid instructor ID")
        
        new_course = Course(**course_data.model_dump())
        return self.course_repo.create(new_course)