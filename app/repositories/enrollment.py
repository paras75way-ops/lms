from sqlmodel import Session, select, and_
from app.models.enrollment import Enrollment

class EnrollmentRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_enrollment(self, student_id: int, course_id: int):
        statement = select(Enrollment).where(
            and_(Enrollment.student_id == student_id, Enrollment.course_id == course_id)
        )
        return self.session.exec(statement).first()

    def create(self, enrollment: Enrollment) -> Enrollment:
        self.session.add(enrollment)
        self.session.commit()
        self.session.refresh(enrollment)
        return enrollment
    
    
    def get_enrollments_by_course(self, course_id: int):
        from sqlmodel import select
        statement = select(Enrollment).where(Enrollment.course_id == course_id)
        return self.session.exec(statement).all()