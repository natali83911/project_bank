import logging
import os

current_dir = os.path.dirname(os.path.abspath(__file__))  # Директория src/
project_root = os.path.join(current_dir, "..")  # Переходим на уровень выше (корень проекта)

# Создаем папку logs в корне проекта, если её нет
logs_dir = os.path.join(project_root, "logs")
os.makedirs(logs_dir, exist_ok=True)

# Создаем путь к файлу utils.log
log_file_path = os.path.join(logs_dir, "masks.log")


logger_masks = logging.getLogger(__name__)
file_handler = logging.FileHandler(log_file_path, mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger_masks.addHandler(file_handler)
logger_masks.setLevel(logging.DEBUG)


def get_mask_card_number(user_card_number: str) -> str:
    """Маскирует номер карты, показывая только первые 6 и последние 4 цифры"""

    logger_masks.debug(f"Начинаем маскировать номер карты: {user_card_number}")

    # Убеждаемся, что номер карты имеет правильную длину (16 цифр) и содержит только цифры
    if not user_card_number.isdigit() or len(user_card_number) != 16:
        if " " in user_card_number:
            logger_masks.error("Номер карты не должен содержать пробелы.")
            raise ValueError("Номер карты не должен содержать пробелы.")
        logger_masks.error("Номер карты должен содержать 16 цифр и не содержать букв.")
        raise ValueError("Номер карты должен содержать 16 цифр  и не содержать букв.")

    # Собираем маскированный номер карты
    masked_card_number = f"{user_card_number[:4]} {user_card_number[4:6]}** **** {user_card_number[-4:]}"

    logger_masks.debug(f"Номер карты маскирован: {masked_card_number}")

    return masked_card_number


def get_mask_account(user_account_number: str) -> str:
    """Маскирует номер счета, показывая только последние 4 цифры"""

    logger_masks.debug(f"Начинаем маскировать номер счета: {user_account_number}")

    # Убеждаемся, что номер счета имеет правильную длину и содержит только цифры
    if not user_account_number.isdigit() or len(user_account_number) != 20:
        if " " in user_account_number:
            logger_masks.error("Номер счета не должен содержать пробелы.")
            raise ValueError("Номер счета не должен содержать пробелы.")
        logger_masks.error("Номер счета должен состоять из 20 цифр и не содержать букв.")
        raise ValueError("Номер счета должен состоять из 20 цифр и не содержать букв.")

    # Маскируем номер счета
    masked_account_number = f"**{user_account_number[-4:]}"

    logger_masks.debug(f"Номер счета маскирован: {masked_account_number}")

    return masked_account_number
