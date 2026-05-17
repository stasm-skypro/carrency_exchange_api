"""
Модуль для загрузки конфигурации из переменных окружения.
"""

import os

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

API_KEY: str | None = os.getenv(key="API_KEY")
SECRET_KEY: str | None = os.getenv(key="SECRET_KEY")
ALGORITHM: str | None = os.getenv(key="ALGORITHM")
