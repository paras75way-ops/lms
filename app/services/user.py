from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import hash_password

class UserService:
    def __init__(self, user_repo):
        self.user_repo = user_repo

    def register_user(self, user_data: UserCreate):
        user_dict = user_data.model_dump()
        plain_password = user_dict.pop("password") 
        user_dict["hashed_password"] = hash_password(plain_password)
        new_user = User(**user_dict)
        return self.user_repo.create(new_user)