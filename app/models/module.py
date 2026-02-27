from typing import Optional
from sqlmodel import Field
from app.models.base import TimestampModel

class Module(TimestampModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(index=True)
    content_type: str = Field(default="video") 
    content_url: Optional[str] = None 
    body_text: Optional[str] = None
    order: int = Field(default=1) 
    
    
    course_id: int = Field(foreign_key="course.id", nullable=False)