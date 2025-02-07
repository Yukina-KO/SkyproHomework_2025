import os
from typing import Union

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def convert_to_rub(transaction: dict) -> Union[float, str]:
    """
    Возвращает сумму транзакции в рублях.
    """
    amount = transaction.get("operationAmount", {}).get("amount")
    currency = transaction.get("operationAmount", {}).get("currency", {}).get("code")
    value_rub = "RUB"
    payload: dict = {}

    if amount and currency:
        if currency != value_rub:
            headers = {"apikey": f"{API_KEY}"}
            response = requests.request(
                "GET",
                f"https://api.apilayer.com/exchangerates_data/convert?to={value_rub}&from={currency}&amount={amount}",
                headers=headers,
                data=payload,
            )
            if response.status_code == 200:
                result = response.json().get("result")  # Получаем числовое значение
                if result is not None:
                    return float(result)
                else:
                    return "Ошибка: Некорректный ответ API"
            else:
                return "Во время конвертации произошла ошибка"
        else:
            return float(amount)  # Если валюта уже RUB, просто возвращаем float
    else:
        return "Данные отсутствуют"
