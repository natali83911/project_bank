from typing import Any, List

import pytest


# Фикстура для генерации номера карты
@pytest.fixture
def valid_card_number() -> str:
    return "7000792289606361"


# Фикстура для генерации номера счета
@pytest.fixture
def valid_account_number() -> str:
    return "73654108430135874305"


# Фикстуры для генерации списка словарей
@pytest.fixture
def list_dict_info() -> List[Any]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def list_dict_info_same_date() -> List[Any]:
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-01-01T00:00:00"},
        {"id": 2, "state": "EXECUTED", "date": "2023-01-01T00:00:00"},
        {"id": 3, "state": "CANCELED", "date": "2023-01-01T00:00:00"},
    ]


@pytest.fixture
def list_dict_info_invalid_date() -> List[Any]:
    return [{"id": 1, "state": "EXECUTED", "date": "2023-01-01"}, {"id": 2, "state": "EXECUTED", "date": "01-02-2025"}]


@pytest.fixture
def list_dict_info_empty() -> List[Any]:
    return []

