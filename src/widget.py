from typing import Union

from .masks import get_mask_account, get_mask_card_number


def mask_account_card(user_bank_details: str) -> str:
    """функция обрабатывает информацию о карте или счете клиента и маскирует номер"""
    numbers_bank_details = ""  # инициализация пустой строки для номера карты/счета
    name_bank_details = ""  # инициализация пустой строки для имени карты/счета
    for char in user_bank_details:  # итерация по символам строки
        if char.isdigit():  # проверка на цифру и добавление в строку с номером
            numbers_bank_details += char
        elif char.isalpha() or char.isspace():  # Проверка на букву или пробел и добавление в строку с именем
            name_bank_details += char
    if len(numbers_bank_details) == 16:  # проверка по количеству цифр номера карты и маскировка номера
        masked_card_number = f"{name_bank_details} {get_mask_card_number(numbers_bank_details)}"
        return masked_card_number
    elif len(numbers_bank_details) == 20:
        # Используем функцию get_mask_account для маскировки номера счета
        masked_account_number = f"{name_bank_details} {get_mask_account(numbers_bank_details)}"
        return masked_account_number
    else:
        return "Неверный формат номера карты или счета"


def get_date(date_string: str) -> str:
    """функция преобразует дату в формат 'ДД.ММ.ГГГГ'"""
    # Разделение строки на 2 части по "Т", а также по "-" части строки с индексом 0
    parts = date_string.split("T")[0].split("-")

    # Извлечение год, месяц, день
    year, month, day = parts

    # Форматирование даты в нужный формат
    formatted_date = f"{day}.{month}.{year}"

    return formatted_date
