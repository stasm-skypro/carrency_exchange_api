"""
Модуль для загрузки конфигурации из переменных окружения.
"""

import os

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

API_KEY: str | None = os.getenv(key="API_KEY")
