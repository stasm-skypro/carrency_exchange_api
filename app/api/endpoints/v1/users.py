"""
Модуль API для управления пользователями.
"""

from fastapi import APIRouter

from app.api.schemas.user import UserLogin

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/login")
def login_user(payload: UserLogin) -> dict:
    """
    Логин пользователя.
    """
    return {"message": "User logged in successfully"}


@router.get("/me")
def get_current_user() -> dict:
    """
    Получение информации о текущем пользователе.
    """
    return {"username": "current_user", "email": "current_user@example.com"}
