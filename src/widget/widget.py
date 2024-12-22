from src import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """
    Функция для маскировки счетов и кард
    :param account_card: счет или карта
    :return: Возвращает зашифрованный счет или карту
    """
    if account_card[0:4] == "Счет" or account_card[0:4] == "Счёт":
        return account_card.replace(account_card[-20:], get_mask_account(account_card[-20:]))
    else:
        return account_card.replace(account_card[-16:], get_mask_card_number(account_card[-16:]))


def get_date(date: str) -> str:
    """
    Функция для преобразования даты из одного формата в другой
    :param date: дата
    :return: возвращает дату в формате "ДД.ММ.ГГГГ"
    """
    date_split = date[0:10].split("-")
    return f"{date_split[2]}.{date_split[1]}.{date_split[0]}"
