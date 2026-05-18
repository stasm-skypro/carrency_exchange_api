"""
Модуль API для управления пользователями с испоьзованием OAuth2.
"""

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException

from app.api.schemas.user import UserLogin
from app.core.security import FAKE_USERS, create_access_token, get_current_user

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
def get_me(current_user: Annotated[dict, Depends(get_current_user)]) -> dict:
    """
    Получение информации о текущем пользователе.
    """

    return {"username": current_user["username"]}
