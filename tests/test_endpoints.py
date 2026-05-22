"""
Модуль для тестирования API.
"""

import pytest
from fastapi.testclient import TestClient

from main import app

FAKE_TEST_DB = dict()

client = TestClient(app)


# Фикстура для очистки тестовой базы данных перед каждым тестом
@pytest.fixture(autouse=True)
def clean_fake_db():
    FAKE_TEST_DB.clear()
    yield


def test_register_user_success() -> None:
    """
    Тест успешной регистрации пользователя.
    """
    response = client.post(
        "/api/v2/auth/register",
        json={"username": "testuser", "password": "testpass", "password_confirm": "testpass"},
    )
    assert response.status_code == 200
    assert response.json() == {"username": "testuser", "password": "testpass"}


def test_register_user_wrong_password_confirm() -> None:
    """
    Тест регистрации пользователя с неправильным подтверждением пароля.
    """
    response = client.post(
        "/api/v2/auth/register",
        json={"username": "testuser", "password": "testpass", "password_confirm": "wrongpass"},
    )
    assert response.status_code == 422
    assert response.json()["detail"][0]["msg"] == "Value error, password_confirm does not match password"


def test_register_user_existing_username() -> None:
    """
    Тест регистрации пользователя с уже существующим именем пользователя.
    """
    # Сначала регистрируем пользователя
    client.post(
        "/api/v2/auth/register",
        json={"username": "testuser", "password": "testpass", "password_confirm": "testpass"},
    )
    # Пытаемся зарегистрировать другого пользователя с тем же именем
    response = client.post(
        "/api/v2/auth/register",
        json={"username": "testuser", "password": "newpass", "password_confirm": "newpass"},
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "Username already registered"
