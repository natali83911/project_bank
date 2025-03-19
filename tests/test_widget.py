import pytest
from src.widget import mask_account_card, get_date


# Параметризация для проверки различных кейсов функции маскировки номера карты и счета
@pytest.mark.parametrize("bank_details, expected", [
    ("Visa Classic 1234567890123456", "Visa Classic 1234 56** **** 3456"),
    ("Mastercard 9876543210987654", "Mastercard 9876 54** **** 7654"),
    ("Счет 12345678901234567890", "Счет **7890"),
])
def test_mask_account_card(bank_details: str, expected: str) -> None:
    assert mask_account_card(bank_details) == expected


# Тест на некорректные данные (номер карты/счета неверной длины)
def test_mask_account_card_invalid_length() -> None:
    assert mask_account_card("Visa 1234567890123") == "Неверный формат номера карты или счета"

# Тест на пустую строку
def test_mask_account_card_empty() -> None:
    assert mask_account_card("") == "Неверный формат номера карты или счета"

# Тест на строку без цифр
def test_mask_account_card_no_numbers() -> None:
    assert mask_account_card("Visa Classic") == "Неверный формат номера карты или счета"


def test_get_date(valid_date_string):
    assert get_date(valid_date_string) == "26.10.2023"


# Параметризация для разных форматов даты
@pytest.mark.parametrize("date_string, expected", [
    ("2023-10-26T00:00:00", "26.10.2023"),
    ("2024-01-01T12:00:00", "01.01.2024"),
])
def test_get_date(date_string: str, expected: str) -> None:
    assert get_date(date_string) == expected

# Тест на некорректные данные (неправильный формат даты)
def test_get_date_invalid_format() -> None:
    with pytest.raises(ValueError):
        get_date("26.10.2023T00:00:00")

# Тест на пустую строку
def test_get_date_empty() -> None:
    with pytest.raises(ValueError):
        get_date("")

# Тест на строку без разделителя "T"
def test_get_date_no_t_separator() -> None:
    with pytest.raises(ValueError):
        get_date("2023-10-26")
