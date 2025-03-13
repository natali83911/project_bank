def get_mask_card_number(user_card_number: str) -> str:
    """Маскирует номер карты, показывая только первые 6 и последние 4 цифры"""

    # Убеждаемся, что номер карты имеет правильную длину (16 цифр)
    if len(user_card_number) != 16:

        raise ValueError("Номер карты должен содержать 16 цифр.")

    # Собираем маскированный номер карты
    masked_card_number = f"{user_card_number[:4]} {user_card_number[4:6]}** **** {user_card_number[-4:]}"

    return masked_card_number


def get_mask_account(user_account_number: str) -> str:
    """Маскирует номер счета, показывая только последние 4 цифры"""

    # Убеждаемся, что номер счета имеет правильную длину
    if len(user_account_number) != 20:
        raise ValueError("Номер счета должен состоять из 20 цифр.")

    # Маскируем номер счета
    masked_account_number = f"**{user_account_number[-4:]}"

    return masked_account_number
