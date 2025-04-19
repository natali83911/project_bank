import csv

import pandas as pd


def count_fin_transactions_csv(file_path):
    """Функция для считывания финансовых операций из CSV файла и возврата списка словарей"""
    transaction_list = []
    try:
        with open(file_path, encoding="utf8") as file:
            reader = csv.DictReader(file, delimiter=";")
            for row in reader:
                transaction_list.append(row)
        return transaction_list
    except FileNotFoundError:
        print(f"Файл не найден по пути: {file_path}")
        return []
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")
        return []


def count_fin_transactions_excel(file_path):
    """Функция для считывания финансовых операций из XLSX-файла и возврата списка словарей."""
    try:
        # Читаем Excel файл
        df = pd.read_excel(file_path)
        # Преобразуем DataFrame в список словарей (по одному на строку)
        transaction_list = df.to_dict(orient="records")
        return transaction_list
    except FileNotFoundError:
        print(f"Файл не найден по пути: {file_path}")
        return []
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")
        return []
