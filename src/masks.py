def get_mask_card_number(card_number: int) -> str:
    """
    Функция преобразования номера карты в "полный" зашифрованный номер
    :param card_number: номер карты пользователя
    :return: зашифрованный номер карты пользователя
    """
    card_number_str = str(card_number)
    if len(card_number_str) == 16:
        return f"{card_number_str[0:5]} {card_number_str[4:6]}** **** {card_number_str[12:17]}"
    else:
        return "Некорректный номер"


def get_mask_account(account_number: int) -> str:
    """
    Функция преобразования номера счета в короткий зашифрованный номер
    :param account_number: номер счета пользователя
    :return: зашифрованный номер счета пользователя
    """
    account_number_str = str(account_number)
    return "**" + account_number_str[-4:]
