"""
Модуль сервисного слоя для работы с пользователями.
"""

from fastapi import HTTPException

from app.api.repository import users as users_repo
from app.api.schemas.user import UserRegister


def create_user(user_data: UserRegister):
    """
    Создает нового пользователя.
    """

    username = user_data.username
    password = user_data.password

    if users_repo.get_user(username):
        raise HTTPException(status_code=400, detail="Username already registered")

    return users_repo.create_user(username, password)


def get_user(username: str) -> dict[str, str]:
    """
    Возвращает пользователя по имени.
    """

    user = users_repo.get_user(username)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
