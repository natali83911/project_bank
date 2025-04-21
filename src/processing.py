from datetime import datetime
from typing import Any, List


def filter_by_state(list_dict_info: List[Any], state: str = "EXECUTED") -> List[Any]:
    """Функция фильтрует данные по указанному параметру"""
    new_filter_list = []
    for element in list_dict_info:
        if element.get("state") == state:
            new_filter_list.append(element)
    return new_filter_list


def sort_by_date(list_dict: List[Any], reverse: bool = True) -> List[Any]:
    """Сортирует список словарей на основе ключа 'date'"""
    for item in list_dict:
        try:
            datetime.fromisoformat(item["date"])
        except ValueError:
            raise ValueError(f"Некорректный формат даты: {item['date']}")

    return sorted(list_dict, key=lambda x: x["date"], reverse=reverse)
