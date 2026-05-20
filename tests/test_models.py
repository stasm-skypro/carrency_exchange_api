"""
Модуль для тестирования моделей (схем) Pydantic.
"""

import pytest
from pydantic import ValidationError
from app.api.schemas.user import UserRegister


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
