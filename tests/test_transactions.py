import json
import os
from unittest.mock import MagicMock, mock_open, patch

import pytest
# import requests_mock
from dotenv import load_dotenv

from src.external_api.external_api import convert_to_rub
# Импортируем функции, которые будем тестировать
from src.utils.transaction import get_transactions

# Загружаем переменные окружения
load_dotenv()


def test_get_transactions() -> None:
    mock_data = [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2023-01-01",
            "operationAmount": {"amount": "100", "currency": {"name": "USD", "code": "USD"}},
        },
        {
            "id": 2,
            "state": "CANCELED",
            "date": "2023-01-02",
            "operationAmount": {"amount": "200", "currency": {"name": "RUB", "code": "RUB"}},
        },
    ]
    mock_json = json.dumps(mock_data)

    with patch("builtins.open", mock_open(read_data=mock_json)), patch("os.path.join", return_value="mocked_path"):
        with patch("json.load", return_value=mock_data):
            transactions = get_transactions()
            assert transactions is None  # Проверяем, что функция не возвращает данных, а только печатает


# Тест для функции convert_to_rub
def test_convert_to_rub() -> None:
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.text = json.dumps({"result": 7500.0})  # Возвращаем JSON-строку

    transaction = {"operationAmount": {"amount": "100", "currency": {"code": "USD"}}}

    with patch("requests.request", return_value=mock_response):
        result = convert_to_rub(transaction)
        assert result == mock_response.text  # Ожидаем строку JSON

    # Тест для случая ошибки API
    mock_response.status_code = 500
    with patch("requests.request", return_value=mock_response):
        result = convert_to_rub(transaction)
        assert result == "Во время конвертации произошла ошибка"

    # Тест для RUB → RUB (функция просто возвращает исходные данные)
    transaction_rub = {"operationAmount": {"amount": "100", "currency": {"code": "RUB"}}}
    result = convert_to_rub(transaction_rub)
    assert result == transaction_rub

    # Тест для случая, когда данные отсутствуют
    transaction_no_data: dict = {}
    result = convert_to_rub(transaction_no_data)
    assert result == "Данные отсутствуют"
