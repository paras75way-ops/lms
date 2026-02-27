from sqlmodel import Session, select
from app.models.user import User

class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, user: User) -> User:
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    def get_by_id(self, user_id: int):
        return self.session.get(User, user_id)

    def get_by_username(self, full_name: str):
        return self.session.exec(select(User).where(User.full_name ==full_name)).first()