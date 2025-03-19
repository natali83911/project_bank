import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number(valid_card_number: str) -> None:
    assert get_mask_card_number(valid_card_number) == "7000 79** **** 6361"


# Параметризация для проверки различных кейсов функции маскировки номера карты
@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("9876543210987654", "9876 54** **** 7654"),
    ],
)
def test_mask_card_number(card_number: str, expected: str) -> None:
    assert get_mask_card_number(card_number) == expected


# Тест на граничный случай: номер карты короче 16 цифр
def test_mask_card_number_short(valid_card_number: str) -> None:
    with pytest.raises(ValueError):
        get_mask_card_number(valid_card_number[:-1])  # Удаляем одну цифру


# Тест на граничный случай: номер карты длиннее 16 цифр
def test_mask_card_number_long(valid_card_number: str) -> None:
    with pytest.raises(ValueError):
        get_mask_card_number(valid_card_number + "1")  # Добавляем одну цифру


# Тест на пустую строку
def test_mask_card_number_empty() -> None:
    with pytest.raises(ValueError):
        get_mask_card_number("")


# Тeст на буквы и пробелы
def test_mask_card_number_with_letters_and_spaces() -> None:
    with pytest.raises(ValueError):
        get_mask_card_number("1234 5678 9012 ab")


# Параметризация для проверки различных кейсов функции маскировки номера счета
@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("73654108430135874305", "**4305"),
        ("98765432109876543210", "**3210"),
    ],
)
def test_mask_account_number(account_number: str, expected: str) -> None:
    assert get_mask_account(account_number) == expected


# Тест на граничный случай: номер счета короче 20 цифр
def test_mask_account_number_short(valid_account_number: str) -> None:
    with pytest.raises(ValueError):
        get_mask_account(valid_account_number[:-1])  # Удаляем одну цифру


# Тест на граничный случай: номер счета длиннее 20 цифр
def test_mask_account_number_long(valid_account_number: str) -> None:
    with pytest.raises(ValueError):
        get_mask_account(valid_account_number + "1")  # Добавляем одну цифру


# Тест на пустую строку
def test_mask_account_number_empty() -> None:
    with pytest.raises(ValueError):
        get_mask_account("")


# Тeст на буквы и пробелы
def test_mask_account_number_with_letters_and_spaces() -> None:
    with pytest.raises(ValueError):
        get_mask_account("1234 5678 9012 3456 789a")
