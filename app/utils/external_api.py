"""
Модуль для получения курсов валют из внешнего API.
"""

import requests

from app.api.schemas.currency import CurrencyExchangeRequest
from app.core.config import API_KEY


def get_supported_currencies() -> dict:
    """
    Возвращает список поддерживаемых валют из внешнего API.
    Пример ответа:
    {
        "result":"success",
        "documentation":"https://www.exchangerate-api.com/docs",
        "terms_of_use":"https://www.exchangerate-api.com/terms"
        "supported_codes":[
                ["AED","UAE Dirham"],
                ["AFN","Afghan Afghani"],
                ["ALL","Albanian Lek"],
                ["AMD","Armenian Dram"],
                ["ANG","Netherlands Antillian Guilder"],
                ["AOA","Angolan Kwanza"],
                ["ARS","Argentine Peso"],
                ["AUD","Australian Dollar"],
                ["AWG","Aruban Florin"],
                ["AZN","Azerbaijani Manat"],
                ["BAM","Bosnia and Herzegovina Convertible Mark"],
                ["BBD","Barbados Dollar"],
                etc.
                etc.
        ]
    }
    Ответ в случае ошибки:
    {
        "result": "error",
        "error-type": "invalid-key"
    }
    """

    try:
        url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/codes"
        response = requests.get(url)
        data = response.json()
        return data

    except requests.RequestException as e:
        return {"result": "error", "error-type": str(e)}


def get_currency_rates(base: str) -> dict:
    """
    Возвращает обменные курсы для различных валют относительно базовой валюты из внешнего API.
    Пример ответа:
    {
        "result": "success",
        "documentation": "https://www.exchangerate-api.com/docs",
        "terms_of_use": "https://www.exchangerate-api.com/terms",
        "time_last_update_unix": 1585267200,
        "time_last_update_utc": "Fri, 27 Mar 2020 00:00:00 +0000",
        "time_next_update_unix": 1585353700,
        "time_next_update_utc": "Sat, 28 Mar 2020 00:00:00 +0000",
        "base_code": "USD",
        "conversion_rates": {
                "USD": 1,
                "AUD": 1.4817,
                "BGN": 1.7741,
                "CAD": 1.3168,
                "CHF": 0.9774,
                "CNY": 6.9454,
                "EGP": 15.7361,
                "EUR": 0.9013,
                "GBP": 0.7679,
                "...": 7.8536,
                "...": 1.3127,
                "...": 7.4722, etc. etc.
        }
    }
    Ответ в случае ошибки:
    {
        "result": "error",
        "error-type": "unknown-code"
    }
    """

    try:
        url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{base}"
        response = requests.get(url)
        data = response.json()
        return data

    except requests.RequestException as e:
        return {"result": "error", "error-type": str(e)}


def convert_pair(params: CurrencyExchangeRequest) -> dict:
    """
    Конвертирует сумму из одной валюты в другую с помощью внешнего API.
    Пример ответа:
    {
        "result": "success",
        "documentation": "https://www.exchangerate-api.com/docs",
        "terms_of_use": "https://www.exchangerate-api.com/terms",
        "time_last_update_unix": 1585267200,
        "time_last_update_utc": "Fri, 27 Mar 2020 00:00:00 +0000",
        "time_next_update_unix": 1585270800,
        "time_next_update_utc": "Sat, 28 Mar 2020 01:00:00 +0000",
        "base_code": "EUR",
        "target_code": "GBP",
        "conversion_rate": 0.8412,
        "conversion_result": 84.12
    }
    Ответ в случае ошибки:
    {
        "result": "error",
        "error-type": "unknown-code"
    }
    """

    try:
        url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{params.currency_from}/{params.currency_to}/{params.amount}"
        response = requests.get(url)
        data = response.json()
        return data

    except requests.RequestException as e:
        return {"result": "error", "error-type": str(e)}
