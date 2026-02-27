from typing import Optional
from sqlmodel import SQLModel, Field, UniqueConstraint
from app.models.base import TimestampModel

class Enrollment(TimestampModel, table=True):
    __table_args__ = (UniqueConstraint("student_id", "course_id", name="unique_enrollment"),)

    id: Optional[int] = Field(default=None, primary_key=True)
    student_id: int = Field(foreign_key="user.id", nullable=False)
    course_id: int = Field(foreign_key="course.id", nullable=False)
    is_active: bool = Field(default=True)
