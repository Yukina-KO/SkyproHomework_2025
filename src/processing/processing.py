from datetime import datetime
from typing import List, Dict


def filter_by_state(input_list: List[Dict], state_default: str = "EXECUTED") -> List[Dict]:
    """
    Функция для отбора словарей по параметру state_default
    :param input_list: список из словарей
    :param state_default: статус
    :return: Возвращает новый список из словарей, у которого ключ "state" соответствует параметру state_default
    """
    new_list = []
    for element in input_list:
        if state_default == "EXECUTED":
            if element["state"] == state_default:
                new_list.append(element)
        elif state_default == "CANCELED":
            if element["state"] == state_default:
                new_list.append(element)
    return new_list


def sort_by_date(input_list: List[Dict], sort_increase: bool = True) -> List[Dict]:
    """
    Функция для сортировки списка из словарей по дате
    :param input_list: список из словарей
    :param sort_increase: сортировка по возрастанию вкл/выкл
    :return: Возвращает отсортированный список из словарей по дате по убыванию/возрастанию
    """
    if sort_increase:
        return sorted(input_list, key=lambda x: datetime.fromisoformat(x["date"]))
    else:
        return sorted(input_list, key=lambda x: datetime.fromisoformat(x["date"]), reverse=True)
