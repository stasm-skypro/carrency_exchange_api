"""
Модуль содержит схемы данных, используемые в API для работы с валютами. Эти схемы описывают структуру данных
при запросах к API, а также возможные ошибки, которые могут возникать при работе с валютами.
"""

from decimal import Decimal

from pydantic import BaseModel, Field

CURRENCY_PATTERN = r"^[a-zA-Z]{3}$"


class CurrencyExchangeRequest(BaseModel):
    """
    Схема данных для обменного курса валюты. Представляет собой строку, которая
    может содержать код валюты и ее обменный курс относительно базовой валюты.
    Например: "USD: 1.0", "EUR: 0.85", "JPY: 110.0" и т.д.
    -- `currency_from`: Код валюты, которую нужно конвертировать (например, "USD").
    -- `currency_to`: Код валюты, в которую нужно конвертировать (например, "RUB").
    -- `amount`: Сумма, которую нужно конвертировать (например, 100.0).
    """

    currency_from: str = Field(
        ...,
        description="Currency code to convert from (e.g., 'USD')",
        pattern=CURRENCY_PATTERN,
    )
    currency_to: str = Field(
        ...,
        description="Currency code to convert to (e.g., 'RUB')",
        pattern=CURRENCY_PATTERN,
    )
    amount: Decimal = Field(
        default=Decimal(0),
        ge=Decimal(0),
        description="Amount must be a positive number",
    )
