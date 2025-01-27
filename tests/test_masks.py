import pytest

from src.masks.masks import get_mask_account, get_mask_card_number


# Тесты для get_mask_card_number
def test_get_mask_card_number_valid() -> None:
    """Тестирование правильности маскирования номера карты."""
    assert get_mask_card_number("1234567812345678") == "12345 56** **** 5678"


def test_get_mask_card_number_incorrect_length() -> None:
    """Проверка обработки некорректных длин номера карты."""
    assert get_mask_card_number("12345678") == "Некорректный номер"
    assert get_mask_card_number("12345678123456789") == "Некорректный номер"


def test_get_mask_card_number_empty() -> None:
    """Проверка обработки пустой строки как номера карты."""
    assert get_mask_card_number("") == "Некорректный номер"


def test_get_mask_card_number_non_digit() -> None:
    """Проверка обработки строки с нецифровыми символами."""
    assert get_mask_card_number("abcd1234abcd5678") == "Некорректный номер"


# Тесты для get_mask_account
def test_get_mask_account_valid() -> None:
    """Тестирование правильности маскирования номера счета."""
    assert get_mask_account("12345678901234567890") == "**7890"


def test_get_mask_account_incorrect_length() -> None:
    """Проверка обработки некорректной длины номера счета."""
    assert get_mask_account("1234567890123456789") == "Некорректный номер"
    assert get_mask_account("123456789012345678901") == "Некорректный номер"


def test_get_mask_account_empty() -> None:
    """Проверка обработки пустого номера счета."""
    assert get_mask_account("") == "Некорректный номер"


def test_get_mask_account_non_digit() -> None:
    """Проверка обработки строки с нецифровыми символами как номера счета."""
    assert get_mask_account("abcd1234567890123456") == "Некорректный номер"
    assert get_mask_account("1234abcd567890123456") == "Некорректный номер"


@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("12345678901234567890", "**7890"),
        ("12345678", "Некорректный номер"),
        ("1234abcd567890123456", "Некорректный номер"),
        ("abcd1234567890123456", "Некорректный номер"),
    ],
)
def test_get_mask_account_parametrized(account_number: str, expected: str) -> None:
    """Параметризованные тесты для get_mask_account."""
    assert get_mask_account(account_number) == expected


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("1234567812345678", "12345 56** **** 5678"),
        ("1234abcd5678", "Некорректный номер"),
        ("12345678", "Некорректный номер"),
        ("abcd123456781234", "Некорректный номер"),
    ],
)
def test_get_mask_card_number_parametrized(card_number: str, expected: str) -> None:
    """Параметризованные тесты для get_mask_card_number."""
    assert get_mask_card_number(card_number) == expected
