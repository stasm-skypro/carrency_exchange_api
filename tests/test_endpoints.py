"""
Модуль для тестирования API.
"""

import pytest
from fastapi.testclient import TestClient

from main import app

FAKE_USERS_DB = dict()

client = TestClient(app)


@pytest.fixture(autouse=True)
def clean_fake_db():
    FAKE_USERS_DB.clear()
    yield


def test_register_user_success():
    response = client.post(
        "/api/v2/auth/register",
        json={"username": "testuser", "password": "testpass", "password_confirm": "testpass"},
    )
    assert response.status_code == 200
    assert "testuser" in FAKE_USERS_DB
    assert response.json() == {"message": "User testuser registered successfully"}
