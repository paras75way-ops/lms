from pydantic import BaseModel
from datetime import datetime

 
class ProgressRead(BaseModel):
    id: int
    student_id: int
    module_id: int
    is_completed: bool
    updated_at: datetime

    class Config:
        from_attributes = True

 
class CourseProgressResponse(BaseModel):
    total_modules: int
    completed_modules: int
    completion_percentage: float
    is_course_finished: bool