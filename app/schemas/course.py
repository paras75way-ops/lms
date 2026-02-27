from pydantic import BaseModel
from typing import Optional


class CourseCreateRequest(BaseModel):
    title: str
    description: str


class CourseCreate(BaseModel):
    title: str
    description: str
    instructor_id: int


class CourseRead(BaseModel):
    id: int
    title: str
    description: str
    instructor_id: int

    class Config:
        from_attributes = True