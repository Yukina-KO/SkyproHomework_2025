from typing import Dict, Hashable, List

import pandas as pd


def read_transactions_csv(file_path: str) -> List[Dict[Hashable, str]]:
    """
    Читает финансовые операции из CSV-файла и возвращает список словарей.
    :param file_path: Путь к CSV-файлу.
    :return: Список словарей с транзакциями.
    """
    df = pd.read_csv(file_path, sep=";")
    return df.to_dict(orient="records")


def read_transactions_excel(file_path: str) -> List[Dict[Hashable, str]]:
    """
    Читает финансовые операции из Excel-файла и возвращает список словарей.
    :param file_path: Путь к Excel-файлу.
    :return: Список словарей с транзакциями.
    """
    df = pd.read_excel(file_path)
    return df.to_dict(orient="records")
