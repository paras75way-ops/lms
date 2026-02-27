from sqlmodel import Session, select
from app.models.course import Course

class CourseRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, course: Course) -> Course:
        self.session.add(course)
        self.session.commit()
        self.session.refresh(course)
        return course

    def get_all(self):
        return self.session.exec(select(Course)).all()

    def get_by_id(self, course_id: int):
        return self.session.get(Course, course_id)

    def get_courses_by_instructor(self, instructor_id: int):
        from sqlmodel import select
        statement = select(Course).where(Course.instructor_id == instructor_id)
        return self.session.exec(statement).all()    