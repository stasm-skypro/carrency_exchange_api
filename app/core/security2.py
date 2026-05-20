from typing import Annotated

from datetime import UTC, datetime, timedelta
import jwt
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

from app.core.config import ALGORITHM, SECRET_KEY

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/oauth/login")


def create_access_token(data: dict) -> str:
    """
    Создаёт токен доступа.
    """
    payload: dict = data.copy()
    payload["exp"] = datetime.now(tz=UTC) + timedelta(minutes=30)

    if SECRET_KEY is None or ALGORITHM is None:
        raise ValueError("SECRET_KEY and ALGORITHM must be set in environment variables")

    return jwt.encode(payload=payload, key=SECRET_KEY, algorithm=ALGORITHM)


def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
) -> dict:
    """
    Получает текущего пользователя из токена доступа.
    """
    if SECRET_KEY is None or ALGORITHM is None:
        raise ValueError("SECRET_KEY and ALGORITHM must be set in environment variables")

    try:
        payload: dict = jwt.decode(jwt=token, key=SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload["sub"]
        return {"username": username}

    except jwt.InvalidTokenError as e:
        raise HTTPException(status_code=401, detail="Invalid token") from e
