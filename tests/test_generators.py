from typing import Dict, List

import pytest

from src.generators.generators import card_number_generator, filter_by_state, transaction_descriptions


# Фикстура для примеров данных
@pytest.fixture
def transactions() -> List[Dict]:
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


# Тесты для filter_by_currency
def test_filter_by_currency_correct_filtering(transactions: List[Dict]) -> None:
    """Проверяем, что фильтрация по валюте USD работает корректно"""
    usd_transactions = list(filter_by_state(transactions, "USD"))
    assert len(usd_transactions) == 3
    assert all(currency["operationAmount"]["currency"]["code"] == "USD" for currency in usd_transactions)


def test_filter_by_currency_no_matching_currency(transactions: List[Dict]) -> None:
    """Проверяем, что функция возвращает пустой результат, если подходящих валют нет"""
    jpy_transactions = list(filter_by_state(transactions, "JPY"))
    assert len(jpy_transactions) == 0


def test_filter_by_currency_empty_list() -> None:
    """Проверяем, что функция корректно обрабатывает пустой список"""
    usd_transactions = list(filter_by_state([], "USD"))
    assert len(usd_transactions) == 0


# Тесты для transaction_descriptions
def test_transaction_descriptions_correct_output(transactions: List[Dict]) -> None:
    """Проверяем, что возвращаются корректные описания транзакций"""
    expected_descriptions = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]
    result = list(transaction_descriptions(transactions))
    assert result == expected_descriptions


def test_transaction_descriptions_empty_list() -> None:
    """Проверяем, что функция корректно обрабатывает пустой список транзакций"""
    descriptions = list(transaction_descriptions([]))
    assert descriptions == []


# Тесты для card_number_generator
def test_card_number_generator_correct_format() -> None:
    """Проверяем, что номера карт генерируются в правильном формате"""
    card_numbers = list(card_number_generator(1, 3))
    assert card_numbers == [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
    ]


def test_card_number_generator_boundary_values() -> None:
    """Проверяем генерацию карт для крайних значений диапазона"""
    card_numbers = list(card_number_generator(9999999999999998, 9999999999999999))
    assert card_numbers == [
        "9999 9999 9999 9998",
        "9999 9999 9999 9999",
    ]


def test_card_number_generator_empty_range() -> None:
    """Проверяем, что генератор корректно обрабатывает пустой диапазон"""
    card_numbers = list(card_number_generator(5, 4))
    assert card_numbers == []
