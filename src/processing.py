from typing import Dict, List


def filter_by_state(list_dict_info: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """Функция фильтрует данные по указанному параметру"""
    new_filter_list = []
    for element in list_dict_info:
        if element["state"] == state:
            new_filter_list.append(element)
    return new_filter_list


def sort_by_date(list_dict: List[Dict], reverse: bool = True) -> List[Dict]:
    """Сортирует список словарей на основе ключа 'date'"""
    return sorted(list_dict, key=lambda x: x["date"], reverse=reverse)
