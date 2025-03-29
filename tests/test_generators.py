from typing import Any, Dict, List

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


# тестирование функции filter_by_currency
# Параметризация для проверки различных кейсов функции выдающий транзакции с указанной валютой
def test_filter_by_currency_usd(transactions: List[Dict[str, Any]]) -> None:
    expected = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
    ]
    result = list(filter_by_currency(transactions, "USD"))
    assert result == expected


def test_filter_by_currency_rub(transactions: List[Dict[str, Any]]) -> None:
    expected = [
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]
    result = list(filter_by_currency(transactions, "RUB"))
    assert result == expected


def test_filter_by_currency_empty(transactions: List[Dict[str, Any]]) -> None:
    result = list(filter_by_currency(transactions, "EUR"))
    assert result == []


def test_filter_by_currency_empty_list() -> None:
    transactions = []
    result = list(filter_by_currency(transactions, "USD"))
    assert result == []


# Тестирование функции transaction_descriptions
# Тесты с параметризацией
@pytest.mark.parametrize(
    "test_input, expected_descriptions",
    [
        # Стандартный случай: возвращаем все описания
        (
            "full_list",
            [
                "Перевод организации",
                "Перевод со счета на счет",
                "Перевод со счета на счет",
                "Перевод с карты на карту",
                "Перевод организации",
            ],
        ),
        # Пустой список транзакций
        ([], []),
        # Одна транзакция
        (
            [
                {
                    "description": "Тестовая транзакция",
                    "operationAmount": {"currency": {"code": "RUB"}},
                }
            ],
            ["Тестовая транзакция"],
        ),
    ],
)
def test_transaction_descriptions(
    test_input: Any, expected_descriptions: List[str], transactions: List[Dict[str, Any]]
) -> None:

    if test_input == "full_list":
        input_data = transactions
    else:
        input_data = test_input

    result = list(transaction_descriptions(input_data))
    assert result == expected_descriptions, f"Ожидались описания: {expected_descriptions}, " f"получены: {result}"


# Тесты для функции card_number_generator


def test_card_number_generator_format() -> None:
    start = 1
    end = 10
    result = list(card_number_generator(start, end))

    for i, card_number in enumerate(result):
        expected_number = "{:016d}".format(i + start)
        formatted_expected = "{} {} {} {}".format(
            expected_number[:4], expected_number[4:8], expected_number[8:12], expected_number[12:]
        )
        assert card_number == formatted_expected


def test_card_number_generator_range() -> None:
    start = 1
    end = 10
    result = list(card_number_generator(start, end))
    assert len(result) == end - start + 1


def test_card_number_generator_edge_cases() -> None:
    start = 0
    end = 0
    result = list(card_number_generator(start, end))
    assert len(result) == 1
    assert result[0] == "0000 0000 0000 0000"


def test_card_number_generator_empty_range() -> None:
    start = 10
    end = 5
    with pytest.raises(ValueError):
        list(card_number_generator(start, end))


def test_card_number_generator_large_range() -> None:
    start = 1
    end = 1000
    result = list(card_number_generator(start, end))
    assert len(result) == end - start + 1
