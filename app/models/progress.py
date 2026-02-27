from typing import Optional
from sqlmodel import Field, UniqueConstraint
from app.models.base import TimestampModel

class Progress(TimestampModel, table=True):
    
    __table_args__ = (UniqueConstraint("student_id", "module_id", name="unique_progress"),)
    
    id: Optional[int] = Field(default=None, primary_key=True)
    is_completed: bool = Field(default=False)
    
   
    student_id: int = Field(foreign_key="user.id", nullable=False)
    module_id: int = Field(foreign_key="module.id", nullable=False)