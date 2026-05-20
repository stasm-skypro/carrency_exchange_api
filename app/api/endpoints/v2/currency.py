"""
Модуль API для получения списка, кодов и курсов валют с испоьзованием OAuth2.
"""

from typing import Annotated

from fastapi import APIRouter, Depends

from app.api.schemas.currency import CurrencyExchangeRequest
from app.core.security import get_current_user
from app.utils import external_api as external_api_service

router = APIRouter(prefix="/currencies")


@router.get("/list")
def get_supported_currencies() -> dict:
    """
    Получает список поддерживаемых валют из открытого API обменных курсов.
    Пример ответа:
    ```json
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
    ```
    """

    return external_api_service.get_supported_currencies()


@router.get("/rates")
def get_currency_list(base: str, current_user: Annotated[dict, Depends(get_current_user)]) -> dict | None:
    """
    Получает свежие обменные курсы для различных валют из открытого API обменных курсов.
    ```json
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
                "...": 7.4722,
                etc.
                etc.
        }
    }
    Ответ в случае ошибки:
    {
        "result": "error",
        "error-type": "unknown-code"
    }
    ```
    """

    if current_user is not None:
        return external_api_service.get_currency_rates(base)
    return None


@router.get("/convert")
def convert_pair(
    params: Annotated[CurrencyExchangeRequest, Depends()], current_user: Annotated[dict, Depends(get_current_user)]
) -> dict | None:
    """
    Осуществляет обмен валют.
    ```json
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
    ```
    """

    if current_user is not None:
        return external_api_service.convert_pair(params)
    return None
