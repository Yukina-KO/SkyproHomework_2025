from typing import Dict, Generator, List


def filter_by_state(input_list: List[Dict], currency: str) -> Generator[dict, None, None]:
    """
    Функция фильтрует транзакции по указанной валюте.
    :param input_list: список словарей, представляющих транзакции
    :param currency: код валюты, по которой требуется фильтрация (например, 'USD')
    :return: генератор с отфильтрованными транзакциями
    """
    return (
        transaction for transaction in input_list if transaction["operationAmount"]["currency"]["code"] == currency
    )


def transaction_descriptions(input_list: list[dict]) -> Generator[str, None, None]:
    """
    Генератор, возвращающий описание каждой операции из списка транзакций.
    :param input_list: список словарей, представляющих транзакции
    :return: генератор строк с описанием операций
    """
    for transaction in input_list:
        yield transaction.get("description", "Описание отсутствует")


def card_number_generator(start: int, end: int) -> Generator[str, None, None]:
    """
    Генератор, возвращающий номера банковских карт в формате XXXX XXXX XXXX XXXX.
    :param start: начальное значение диапазона (включительно)
    :param end: конечное значение диапазона (включительно)
    :yield: номер карты в формате строки XXXX XXXX XXXX XXXX
    """
    for number in range(start, end + 1):
        number_str = str(number).zfill(16)
        yield f"{number_str[:4]} {number_str[4:8]} {number_str[8:12]} {number_str[12:16]}"
