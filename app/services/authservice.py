from fastapi import HTTPException
from jose import jwt, JWTError
from app.core.security import (
    verify_password,
    create_access_token,
    create_refresh_token,
    SECRET_KEY,
    ALGORITHM
)

class AuthService:
    def __init__(self, user_repo):
        self.user_repo = user_repo

    def authenticate_user(self, username: str, password: str):
        user = self.user_repo.get_by_username(username)
        if not user or not verify_password(password, user.hashed_password):
            raise HTTPException(status_code=401, detail="Invalid email or password")

        # Include role in token so deps.py doesn't need extra DB lookup
        access_token = create_access_token(data={"sub": str(user.id), "role": user.role.value})
        refresh_token = create_refresh_token(data={"sub": str(user.id), "role": user.role.value})

        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer",
            "user": {
                "id": user.id,
                "email": user.email,
                "full_name": user.full_name,
                "role": user.role,
            }
        }

    def refresh_access_token(self, refresh_token: str):
        credentials_exception = HTTPException(
            status_code=401,
            detail="Could not validate credentials or token expired",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(refresh_token, SECRET_KEY, algorithms=[ALGORITHM])

            if payload.get("type") != "refresh":
                raise HTTPException(status_code=401, detail="Invalid token type. Must use refresh token.")

            user_id: str = payload.get("sub")
            if user_id is None:
                raise credentials_exception
        except JWTError:
            raise credentials_exception

        user = self.user_repo.get_by_id(int(user_id))
        if not user:
            raise credentials_exception

        new_access_token = create_access_token(data={"sub": str(user.id), "role": user.role.value})

        return {
            "access_token": new_access_token,
            "token_type": "bearer"
        }