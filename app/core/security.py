"""
Модуль для работы с безопасностью.
"""

from datetime import UTC, datetime, timedelta

import jwt
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer

SECRET_KEY = "super-secret-key"
ALGORITHM = "HS256"

security = HTTPBearer()

FAKE_USERS: dict[str, dict[str, str]] = {
    "user1": {
        "username": "user1",
        "password": "password1",
    },
}


def create_access_token(data: dict) -> str:
    """
    Создаёт токен доступа.
    """
    payload: dict = data.copy()
    payload["exp"] = datetime.now(tz=UTC) + timedelta(minutes=30)

    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def get_current_user(credentials=Depends(security)) -> dict:
    """
    Получение информации о текущем пользователе.
    """

    token = credentials.credentials
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM],
        )
        username: str = payload.get("sub")
        return {"username": username}

    except jwt.InvalidTokenError as e:
        raise HTTPException(status_code=401, detail="Invalid token") from e
