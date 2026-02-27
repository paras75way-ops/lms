from enum import Enum
from typing import Optional, List, TYPE_CHECKING
from sqlmodel import Field, Relationship
from app.models.base import TimestampModel
from app.models.enrollment import Enrollment

if TYPE_CHECKING:
    from app.models.course import Course
    from app.models.enrollment import Enrollment

class UserRole(str, Enum):
    INSTRUCTOR = "instructor"
    STUDENT = "student"
    ADMIN = "admin"

class User(TimestampModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(unique=True, index=True, nullable=False)
 
    hashed_password: str = Field(nullable=False) 
    full_name: str = Field(index=True)
    is_active: bool = Field(default=True)
    role: UserRole = Field(default=UserRole.STUDENT)

  
    courses: List["Course"] = Relationship(back_populates="instructor")
    
   
    enrolled_courses: List["Course"] = Relationship(
        back_populates="students", 
        link_model=  Enrollment 
    )