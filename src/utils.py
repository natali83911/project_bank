import json
import os

def load_transactions_from_json(file_path):
    """ Загружает список финансовых транзакций из JSON-файла.
    Возвращает пустой список, если файл не найден, пуст или содержит не список. """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            else:
                return []
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
    except Exception:
        return []


# Пример использования (для проверки)
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if __name__ == '__main__':
    file_path = os.path.join(PROJECT_ROOT, 'data', 'operations.json')
    transactions = load_transactions_from_json(file_path)
    print(transactions)