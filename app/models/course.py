from typing import Optional, TYPE_CHECKING,List
from sqlmodel import SQLModel, Field, Relationship
from app.models.base import TimestampModel
from app.models.enrollment import Enrollment

if TYPE_CHECKING:
    from app.models.user import User
    
class Course(TimestampModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(index=True)
    description: str
    
    
    instructor_id: int = Field(foreign_key="user.id")
    
    
    instructor: "User" = Relationship(back_populates="courses")
   
    students: List["User"] = Relationship(
    back_populates="enrolled_courses", link_model=Enrollment
)