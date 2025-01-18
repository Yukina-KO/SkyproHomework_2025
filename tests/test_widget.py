import pytest

from src.widget.widget import get_date, mask_account_card


# Тесты для mask_account_card
def test_mask_account_card_account() -> None:
    """Тест корректной маскировки для номера счета."""
    account = "Счет 12345678901234567890"
    expected = "Счет **7890"
    assert mask_account_card(account) == expected


def test_mask_account_card_card() -> None:
    """Тест корректной маскировки для номера карты."""
    card = "Mastercard  1234567812345678"
    expected = "Mastercard  12345 56** **** 5678"
    assert mask_account_card(card) == expected


def test_mask_account_card_invalid_account() -> None:
    """Тест обработки некорректного номера счета."""
    account = "Счет 12345678"
    expected = "Некорректный номер"
    assert mask_account_card(account) == expected


def test_mask_account_card_invalid_card() -> None:
    """Тест обработки некорректного номера карты."""
    card = "Карта 1234abcd5678"
    expected = "Некорректный номер"
    assert mask_account_card(card) == expected


@pytest.mark.parametrize(
    "data, expected",
    [
        ("Счет 12345678901234567890", "Счет **7890"),
        ("Карта 1234567812345678", "Карта 12345 56** **** 5678"),
        ("Счет 123", "Некорректный номер"),
        ("Карта abcd1234", "Некорректный номер"),
    ],
)
def test_mask_account_card_parametrized(data: str, expected: str) -> None:
    """Параметризованные тесты для универсальности."""
    assert mask_account_card(data) == expected


# Тесты для get_date
def test_get_date_correct_format() -> None:
    """Тест корректного преобразования даты."""
    date = "2023-12-25"
    expected = "25.12.2023"
    assert get_date(date) == expected


def test_get_date_incorrect_format() -> None:
    """Тест обработки даты с неверным форматом года."""
    date = "23-12-25"
    expected = "Неверный формат даты"
    assert get_date(date) == expected


def test_get_date_empty() -> None:
    """Тест обработки пустой строки как даты."""
    date = ""
    expected = "Неверный формат даты"
    assert get_date(date) == expected


@pytest.mark.parametrize(
    "date, expected",
    [
        ("2023-01-01", "01.01.2023"),
        ("1999-12-31", "31.12.1999"),
        ("2020-02-29", "29.02.2020"),
        ("20-01-01", "Неверный формат даты"),
    ],
)
def test_get_date_parametrized(date: str, expected: str) -> None:
    """Параметризованные тесты для проверки разных форматов даты."""
    assert get_date(date) == expected
