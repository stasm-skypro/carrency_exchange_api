"""
Модуль для загрузки конфигурации из переменных окружения.
"""

import os

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv("API_KEY")
