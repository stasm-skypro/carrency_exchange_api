"""
Модуль API для управления пользователями.
"""

from types import new_class
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from app.api.schemas.user import UserLogin, UserRegister
from app.api.services import users as users_service
from app.core.security import create_access_token, get_current_user

router = APIRouter(prefix="/auth")


@router.post("/register")
def register_user(payload: UserRegister) -> dict:
    """
    Регистрирует новго пользователя.
    -- Если пользователь с таким username уже есть в БД, то возвращает ошибку 400 - Username already registered.
    """

    response = users_service.create_user(payload)

    return response


@router.post("/login")
def login_user(payload: UserLogin) -> dict:
    """
    Аутентифицирует пользователя.
    -- Если пользователь не найден или пароль неверный, возвращает ошибку 401 - Invalid credentials.
    """

    user = users_service.get_user(payload.username)
    password: str = user["password"]

    if password is None or password != payload.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token({"sub": payload.username})

    response = {
        "access_token": access_token,
        "token_type": "bearer",
    }

    return response


@router.get("/me")
def get_me(current_user: Annotated[dict, Depends(get_current_user)]) -> dict:
    """
    Получение информации о текущем пользователе.
    """

    return {"username": current_user["username"]}
