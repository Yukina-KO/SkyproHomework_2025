import os
from typing import Any, Dict, List

from src.generators.generators import count_transactions_by_category, filter_transactions_by_description
from src.transactions.transactions import read_transactions_csv, read_transactions_excel
from src.utils.transaction import get_transactions

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def filter_by_status(transactions: List[Dict[str, Any]], status: str) -> List[Dict[str, Any]]:
    """
    Фильтрует операции по статусу, учитывая разные форматы данных.

    :param transactions: Список транзакций.
    :param status: Желаемый статус (EXECUTED, CANCELED, PENDING).
    :return: Отфильтрованный список транзакций.
    """
    status_upper = status.upper()  # Приводим ввод пользователя к верхнему регистру

    def normalize_status(transaction: Dict[str, Any]) -> str:
        """Приводит статус операции к верхнему регистру, независимо от формата данных."""
        return str(transaction.get("state", transaction.get("State", ""))).strip().upper()

    return [transaction for transaction in transactions if normalize_status(transaction) == status_upper]


def get_choice(choice_values: List[str], message_values: List[str]) -> str:
    """
    Функция для вывода выбора

    :param choice_values: Список возможных выборов.
    :param message_values: Список предложений для выбора пользователя.
    :return: Возвращает результат выбора.
    """
    for message in message_values:
        print(message)

    choice_dict = {}
    count_choice = 1
    for values in choice_values:
        choice_dict[str(count_choice)] = values
        count_choice += 1

    finally_choice = None
    while finally_choice not in choice_values:
        choice = input("Введите номер: ").strip()
        finally_choice = choice_dict.get(choice)
        if not finally_choice:
            print("Ошибка ввода! Выберете нужную категорию.")
            for message in message_values:
                print(message)
    if finally_choice:
        return finally_choice
    return ""


def main() -> None:
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    file_format = get_choice(
        ["json", "csv", "xlsx"],
        [
            "1. Получить информацию о транзакциях из JSON-файла",
            "2. Получить информацию о транзакциях из CSV-файла",
            "3. Получить информацию о транзакциях из XLSX-файла",
        ],
    )

    print(f"Для обработки выбран {file_format.upper()}-файл.")

    file_path = os.path.join(BASE_DIR, "data", f"transactions.{file_format}")
    transactions = None
    if file_format == "json":
        transactions = get_transactions()
    elif file_format == "csv":
        transactions = read_transactions_csv(file_path)
    elif file_format == "xlsx":
        transactions = read_transactions_excel(file_path)

    print("Введите статус:")
    status = get_choice(["EXECUTED", "CANCELED", "PENDING"], ["1. EXECUTED", "2. CANCELED", "3. PENDING"])

    if transactions and status:
        transactions = filter_by_status(transactions, status)

    print(f'Операции отфильтрованы по статусу "{status}"')

    if not transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
        return

    print("Отсортировать операции по дате?")
    sort_choice = get_choice(["да", "нет"], ["1. Да", "2. Нет"])
    if sort_choice == "да":
        print("Отсортировать по возрастанию или по убыванию?")
        order_choice = get_choice(["по возрастанию", "по убыванию"], ["1. По возрастанию", "2. По убыванию"])

        transactions.sort(key=lambda x: x.get("date", ""), reverse=(order_choice == "по убыванию"))

    print("Выводить только рублевые транзакции?")
    currency_choice = get_choice(["да", "нет"], ["1. Да", "2. Нет"])
    if currency_choice == "да":
        if file_format == "json":
            transactions = [
                t for t in transactions if t.get("operationAmount", {}).get("currency", {}).get("code") == "RUB"
            ]
        else:
            transactions = [t for t in transactions if t.get("currency_code", {}) == "RUB"]

    if not transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
        return

    print("Отфильтровать список транзакций по определенному слову в описании?")
    search_choice = get_choice(["да", "нет"], ["1. Да", "2. Нет"])

    if search_choice == "да":
        search_term = input("Введите слово для поиска в описании: ").strip()
        transactions = filter_transactions_by_description(transactions, search_term)

    if not transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
        return

    print("Показать количество операций по категориям?")
    category_choice = get_choice(["да", "нет"], ["1. Да", "2. Нет"])
    if category_choice == "да":

        categories = [
            "Перевод организации",
            "Перевод с карты на карту",
            "Перевод со счета на счет",
            "Открытие вклада",
            "Перевод с карты на счет",
        ]
        category_counts = count_transactions_by_category(transactions, categories)
        print("\nКоличество операций по категориям:")
        for category, count in category_counts.items():
            print(f"{category}: {count}")

    print("Распечатываю итоговый список транзакций...")
    if transactions:
        print(f"Всего банковских операций в выборке: {len(transactions)}")
        for transaction in transactions:
            print(f"{transaction['date'][:10]} {transaction['description']}")
            if "from" in transaction and str(transaction["from"]) != "nan":
                print(f"{transaction['from']} -> {transaction['to']}")
            else:
                print(f"{transaction['to']}")
            if file_format == "json":
                print(
                    f"Сумма: "
                    f"{transaction['operationAmount']['amount']} "
                    f"{transaction['operationAmount']['currency']['code']}\n"
                )
            else:
                print(f"Сумма: " f"{transaction['amount']} " f"{transaction['currency_code']}\n")
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")


if __name__ == "__main__":
    main()
