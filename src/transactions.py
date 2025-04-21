import csv

import pandas as pd


def count_fin_transactions_csv(file_path):
    """Функция для считывания финансовых операций из CSV файла и возврата списка словарей"""
    transaction_list = []
    try:
        with open(file_path, encoding="utf8") as file:
            reader = csv.DictReader(file, delimiter=";")
            for row in reader:
                transaction = {
                    "id": row.get("id"),
                    "state": row.get("state"),
                    "date": row.get("date"),
                    "operationAmount": {
                        "amount": row.get("amount"),
                        "currency": {"name": row.get("currency_name"), "code": row.get("currency_code")},
                    },
                    "description": row.get("description"),
                    "from": row.get("from"),
                    "to": row.get("to"),
                }
                transaction_list.append(transaction)
        return transaction_list
    except FileNotFoundError:
        print(f"Файл не найден по пути: {file_path}")
        return []
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")
        return []


def count_fin_transactions_excel(file_path):
    """Считывает транзакции из Excel файла и возвращает список словарей (Dict)"""
    try:
        df = pd.read_excel(file_path)
        # Преобразуем DataFrame в список словарей (по одному на строку)
        # и сразу создаем структуру, ожидаемую filter_by_currency
        transaction_list = []
        for _, row in df.iterrows():
            transaction = {
                "id": row.get("id"),
                "state": row.get("state"),
                "date": row.get("date"),
                "operationAmount": {
                    "amount": row.get("amount"),
                    "currency": {"name": row.get("currency_name"), "code": row.get("currency_code")},
                },
                "description": row.get("description"),
                "from": row.get("from"),
                "to": row.get("to"),
            }
            transaction_list.append(transaction)

        return transaction_list
    except FileNotFoundError:
        print(f"Файл не найден по пути: {file_path}")
        return []
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")
        return []
