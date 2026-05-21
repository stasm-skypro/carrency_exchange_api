"""
Модуль слоя репозитория для работы с БД.
"""

from app.core.fake_db import FAKE_DB


def create_user(username: str, password: str) -> dict[str, str]:
    """
    Создает нового пользователя и добавляет его в базу данных.
    """
    new_user = {"username": username, "password": password}
    FAKE_DB.append(new_user)
    return new_user


def get_user(username: str) -> dict[str, str] | None:
    """
    Возвращает пользователя по его имени.
    """
    for user in FAKE_DB:
        if user["username"] == username:
            return user
    return None
