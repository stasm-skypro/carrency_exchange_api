"""
Модуль для создания и проверки токенов доступа, и получения информации о пользователе по токену.
"""

from datetime import UTC, datetime, timedelta
from typing import Annotated

import jwt
from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.core.config import ALGORITHM, SECRET_KEY

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

    if SECRET_KEY is None or ALGORITHM is None:
        raise ValueError("SECRET_KEY and ALGORITHM must be set in environment variables")

    return jwt.encode(payload=payload, key=SECRET_KEY, algorithm=ALGORITHM)


def get_current_user(credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)]) -> dict:
    """
    Получение информации о текущем пользователе.
    """

    token: str = credentials.credentials

    if SECRET_KEY is None or ALGORITHM is None:
        raise ValueError("SECRET_KEY and ALGORITHM must be set in environment variables")

    try:
        payload: dict = jwt.decode(
            jwt=token,
            key=SECRET_KEY,
            algorithms=[ALGORITHM],
        )
        username: str = payload["sub"]
        return {"username": username}

    except jwt.InvalidTokenError as e:
        raise HTTPException(status_code=401, detail="Invalid token") from e
