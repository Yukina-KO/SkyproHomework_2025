import re
from collections import defaultdict
from typing import Any, Dict, Generator, List


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


def filter_transactions_by_description(transactions: List[Dict[str, Any]], search_term: str) -> List[Dict[str, Any]]:
    """
    Фильтрует список операций по наличию строки поиска в описании.

    :param transactions: Список словарей с банковскими операциями.
    :param search_term: Строка поиска (используется как часть регулярного выражения).
    :return: Отфильтрованный список словарей.
    """
    pattern = re.compile(re.escape(search_term), re.IGNORECASE)
    return [transaction for transaction in transactions if pattern.search(transaction.get("description", ""))]


def count_transactions_by_category(transactions: List[Dict[str, Any]], categories: List[str]) -> Dict[str, int]:
    """
    Подсчитывает количество операций в каждой категории.

    :param transactions: Список словарей с банковскими операциями.
    :param categories: Список категорий операций.
    :return: Словарь с количеством операций по категориям.
    """
    category_count: defaultdict[Any, int] | defaultdict[str, int] = defaultdict(int)
    for transaction in transactions:
        description = transaction.get("description", "").lower()
        for category in categories:
            if category.lower() in description:
                category_count[category] += 1
    return dict(category_count)
