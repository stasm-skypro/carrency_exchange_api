"""
Модуль для тестирования моделей (схем) Pydantic.
"""

import pytest
from pydantic import ValidationError

from app.api.schemas.user import UserRegister


# Тесты для Pydantic моделей Пользователя
def test_user_register_success():
    """
    Проверяет, что валидная схема UserRegister проходит без ошибок.
    """

    data = {
        "username": "valid_username",
        "password": "strong_pass_123",
        "password_confirm": "strong_pass_123",
    }

    user = UserRegister(**data)
    assert user.username == "valid_username"
    assert user.password == "strong_pass_123"
    assert user.password_confirm == "strong_pass_123"


def test_password_mismatch():
    """
    Проверяет, что схема UserRegister выбрасывает ошибку при несоответствии паролей.
    """

    data = {
        "username": "valid_username",
        "password": "strong_pass_123",
        "password_confirm": "different_pass_456",
    }

    with pytest.raises(ValidationError) as excinfo:
        UserRegister(**data)

    assert "password_confirm does not match password" in str(excinfo.value)


@pytest.mark.parametrize("invalid_username", ["ab", "a" * 21])  # Длина имени min=3 max=20
def test_username_validation(invalid_username):
    """
    Проверяет, что схема UserRegister выбрасывает ошибку при некорректной длине имени пользователя.
    """

    data = {
        "username": invalid_username,  # Длина имени больше 20 символов
        "password": "strong_pass_123",
        "password_confirm": "strong_pass_123",
    }

    with pytest.raises(ValidationError):
        UserRegister(**data)


def test_password_pattern_mismatch():
    """
    Проверяет, что схема UserRegister выбрасывает ошибку при несоответствии пароля паттерну.
    """

    data = {
        "username": "valid_username",
        "password": "weak_pass!#",
        "password_confirm": "weak_pass!#",
    }

    with pytest.raises(ValidationError):
        UserRegister(**data)
