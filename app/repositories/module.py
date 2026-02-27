from sqlmodel import Session, select
from app.models.module import Module

class ModuleRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, module: Module) -> Module:
        self.session.add(module)
        self.session.commit()
        self.session.refresh(module)
        return module

    def get_modules_by_course(self, course_id: int):
        statement = select(Module).where(Module.course_id == course_id).order_by(Module.order)
        return self.session.exec(statement).all()