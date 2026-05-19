"""
Модуль содержит схемы данных, используемые в API для работы с пользователями. Эти схемы описывают структуру данных
при запросах к API, а также возможные ошибки, которые могут возникать при работе с пользователями.
"""

from pydantic import BaseModel, Field, model_validator

from app.core.config import VALID_CHARS


class UserBase(BaseModel):
    """
    Базовая схема для пользователя, содержащая общие поля.
    """

    username: str = Field(..., min_length=3, pattern=VALID_CHARS)


class UserRegister(UserBase):
    """
    Схема для создания пользователя, наследующая от UserBase.
    """

    # Проверяем длинную (не менее чем...) и сложность пароля - допускаются только буквы и цифры
    password: str = Field(..., min_length=4, pattern=VALID_CHARS)
    password_confirm: str = Field(..., min_length=4, pattern=VALID_CHARS)

    @model_validator(mode="before")
    @classmethod
    def password_confirm_matches(cls, values: dict) -> dict:
        if values.get("password") != values.get("password_confirm"):
            raise ValueError("password_confirm does not match password")
        return values


class UserLogin(UserBase):
    """
    Схема для логина пользователя, наследующая от UserBase.
    """

    password: str
