from typing import Any, List

import pytest

from src.processing import filter_by_state, sort_by_date


# Тесты для filter_by_state
# Параметризация для проверки различных кейсов функции фильтрации данных по указанному параметру
@pytest.mark.parametrize(
    "state, expected",
    [
        (
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        ),
        ("PENDING", []),  # Тест на отсутствие словарей с указанным статусом
    ],
)
def test_filter_by_state(list_dict_info: List[Any], state: str, expected: List[Any]) -> None:
    assert filter_by_state(list_dict_info, state) == expected


def test_filter_by_state_empty(list_dict_info_empty: List[Any]) -> None:
    assert filter_by_state(list_dict_info_empty) == []


# Тесты для sort_by_date
def test_sort_by_date_descending(list_dict_info: List[Any]) -> None:
    sorted_list = sort_by_date(list_dict_info)
    assert sorted_list[0]["date"] == "2019-07-03T18:35:29.512364"
    assert sorted_list[-1]["date"] == "2018-06-30T02:08:58.425572"


def test_sort_by_date_ascending(list_dict_info: List[Any]) -> None:
    sorted_list = sort_by_date(list_dict_info, reverse=False)
    assert sorted_list[0]["date"] == "2018-06-30T02:08:58.425572"
    assert sorted_list[-1]["date"] == "2019-07-03T18:35:29.512364"


def test_sort_by_date_same_dates(list_dict_info_same_date: List[Any]) -> None:
    sorted_list = sort_by_date(list_dict_info_same_date)
    assert sorted_list[0]["date"] == "2023-01-01T00:00:00"
    assert sorted_list[-1]["date"] == "2023-01-01T00:00:00"


def test_sort_by_date_invalid_date(list_dict_info_invalid_date: List[Any]) -> None:
    with pytest.raises(ValueError):
        sort_by_date(list_dict_info_invalid_date)
