"""
Модуль API для управления пользователями.
"""

from fastapi import APIRouter, HTTPException

from app.api.schemas.user import UserLogin
from app.core.security import FAKE_USERS, create_access_token

router = APIRouter(prefix="/auth", tags=["authentication"])


@router.post("/login")
def login_user(payload: UserLogin) -> dict:
    """
    Логин пользователя.
    """

    password: str = FAKE_USERS[payload.username]["password"]
    if password is None or password != payload.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token({"sub": payload.username})

    return {
        "access_token": access_token,
        "token_type": "bearer",
    }


@router.get("/me")
def get_current_user() -> dict:
    """
    Получение информации о текущем пользователе.
    """

    return {"username": "current_user", "email": "current_user@example.com"}
