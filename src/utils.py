import json
import logging
import os
from typing import Any, Dict, List

current_dir = os.path.dirname(os.path.abspath(__file__))  # Директория src/
project_root = os.path.join(current_dir, "..")  # Переходим на уровень выше (корень проекта)

# Создаем папку logs в корне проекта, если её нет
logs_dir = os.path.join(project_root, "logs")
os.makedirs(logs_dir, exist_ok=True)

# Создаем путь к файлу utils.log
log_file_path = os.path.join(logs_dir, "utils.log")


logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(log_file_path, mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def load_transactions_from_json(file_path: str) -> List[Dict[str, Any]]:
    """Загружает список финансовых транзакций из JSON-файла.
    Возвращает пустой список, если файл не найден, пуст или содержит не список."""

    logger.debug(f"Начинаем загрузку транзакций из файла: {file_path}")

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            logger.debug(f"Файл {file_path} открыт успешно.")
            data = json.load(f)
            if isinstance(data, list):
                return data
            else:
                logger.warning("Данные не являются списком. Возвращаем пустой список.")
                return []
    except FileNotFoundError:
        logger.error(f"Файл {file_path} не найден.")
        return []
    except json.JSONDecodeError:
        logger.error(f"Ошибка декодирования JSON в файле {file_path}.")
        return []
    except Exception as e:
        logger.critical(f"Критическая ошибка при загрузке файла {file_path}: {str(e)}")
        return []
