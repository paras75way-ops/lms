from typing import Optional
from pydantic import BaseModel
from datetime import datetime

 
class ModuleBase(BaseModel):
    title: str
    content_type: str = "video"  
    content_url: Optional[str] = None
    body_text: Optional[str] = None
    order: int = 1
 
class ModuleCreate(ModuleBase):
    course_id: int

 
class ModuleRead(ModuleBase):
    id: int
    course_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True