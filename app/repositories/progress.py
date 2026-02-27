from sqlmodel import Session, select, and_
from app.models.progress import Progress
from app.models.module import Module 

class ProgressRepository:
    def __init__(self, session: Session):
        self.session = session

    def mark_completed(self, student_id: int, module_id: int) -> Progress:
        statement = select(Progress).where(
            and_(Progress.student_id == student_id, Progress.module_id == module_id)
        )
        progress = self.session.exec(statement).first()
        
        if not progress:
            progress = Progress(student_id=student_id, module_id=module_id, is_completed=True)
        else:
            progress.is_completed = True
            
        self.session.add(progress)
        self.session.commit()
        self.session.refresh(progress)
        return progress

    def check_status(self, student_id: int, module_id: int) -> bool:
        statement = select(Progress).where(
            and_(Progress.student_id == student_id, Progress.module_id == module_id)
        )
        progress = self.session.exec(statement).first()
        return progress.is_completed if progress else False

    def count_completed_modules(self, student_id: int, course_id: int) -> int:

        statement = select(Progress).join(Module, Progress.module_id == Module.id).where(
            and_(
                Progress.student_id == student_id,
                Progress.is_completed == True,
                Module.course_id == course_id
            )
        )
        return len(self.session.exec(statement).all())