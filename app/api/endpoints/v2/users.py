"""
Модуль API для управления пользователями с испоьзованием OAuth2.
"""

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException

from app.api.schemas.user import UserRegister, UserLogin
from app.core.security import FAKE_USERS, create_access_token, get_current_user

router = APIRouter(prefix="/auth")


@router.post("/register")
def register_user(payload: UserRegister) -> dict:
    """
    Регистрация пользователя.
    """
    username: str = payload.username
    password: str = payload.password
    if username in FAKE_USERS:
        raise HTTPException(status_code=400, detail="Username already registered")
    FAKE_USERS[username] = {"password": password}
    return {"message": f"User {username} registered successfully"}


@router.post("/login")
def login_user(payload: UserLogin) -> dict:
    """
    Аутентификация пользователя.
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
