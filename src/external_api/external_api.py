import os
from typing import Union, Dict, Any

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def convert_to_rub(transaction: dict) -> Union[str, Dict[str, Any]]:
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
                f"https://api.apilayer.com/exchangerates_data/convert?to={value_rub}" f"&from={currency}&amount={amount}",
                headers=headers,
                data=payload,
            )
            if response.status_code == 200:
                result = response.text
                return result
            else:
                return "Во время конвертации произошла ошибка"
        else:
            return transaction
    else:
        return "Данные отсутствуют"
