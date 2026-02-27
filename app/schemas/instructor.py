from pydantic import BaseModel
from typing import List

class CourseAnalyticsRead(BaseModel):
    course_id: int
    title: str
    total_students: int
    total_modules: int

class StudentProgressRead(BaseModel):
    student_id: int
    student_email: str
    completion_percentage: float
    is_finished: bool

class InstructorDashboardResponse(BaseModel):
    instructor_id: int
    total_active_courses: int
    total_students_across_courses: int
    courses: List[CourseAnalyticsRead]