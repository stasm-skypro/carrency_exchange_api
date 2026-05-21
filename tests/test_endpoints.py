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


def test_register_user_success():
    """
    Тест успешной регистрации пользователя.
    """
    response = client.post(
        "/api/v2/auth/register",
        json={"username": "testuser", "password": "testpass", "password_confirm": "testpass"},
    )
    assert response.status_code == 200
    assert response.json() == {"username": "testuser", "password": "testpass"}


def test_register_user_failed():
    """
    Тест
    """
    pass
