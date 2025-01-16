from src.masks.masks import get_mask_account, get_mask_card_number
from datetime import datetime


def mask_account_card(account_card: str) -> str:
    """
    Функция для маскировки счетов и кард
    :param account_card: счет или карта
    :return: Возвращает зашифрованный счет или карту
    """
    card_names = ["Карта", "карта", "Visa", "visa", "Mastercard", "mastercard", "Mir", "mir"]
    invoice_names = ["Счет", "счет", "Счёт", "счёт"]
    if any(word in account_card for word in invoice_names):
        if len(account_card[-20:]) == 20 and account_card[-20:].isdigit():
            return account_card.replace(account_card[-20:], get_mask_account(account_card[-20:]))
        else:
            return "Некорректный номер"
    elif any(word in account_card for word in card_names):
        if len(account_card[-16:]) == 16 and account_card[-16:].isdigit():
            return account_card.replace(account_card[-16:], get_mask_card_number(account_card[-16:]))
        else:
            return "Некорректный номер"
    else:
        return "Некорректный номер"


def get_date(date: str) -> str:
    """
    Функция для преобразования даты из одного формата в другой
    :param date: дата
    :return: возвращает дату в формате "ДД.ММ.ГГГГ"
    """
    if not isinstance(date, str) or len(date) < 10:
        return "Неверный формат даты"
    date_split = date.split("-")
    year, month, day = date_split
    if len(date_split) != 3 or len(year) != 4 or len(month) != 2 or len(day) != 2:
        return "Неверный формат даты"

    return f"{day}.{month}.{year}"
