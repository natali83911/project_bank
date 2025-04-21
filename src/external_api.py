import os
from typing import Any, Dict

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def convert_to_rub(transaction: Dict) -> Any:
    """Конвертирует сумму транзакции в рубли.
    Для USD/EUR использует текущий курс через API."""
    operation_amount = transaction.get("operationAmount", {})
    amount = operation_amount.get("amount", 0)
    currency = operation_amount.get("currency", {}).get("code", "RUB").upper()

    if not currency:
        print("Ошибка: Отсутствует код валюты.")
        return None

    if amount and currency:
        try:
            amount = float(amount)
        except ValueError:
            print(f"Ошибка: Некорректный формат суммы: {amount}")
            return None

    if currency == "RUB":
        return amount

    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
    headers = {"apikey": API_KEY}

    try:
        response = requests.get(url, headers=headers)
        status_code = response.status_code

        if status_code == 200:
            return float(response.json()["result"])
        else:
            print(f"Запрос не был успешным. Возможная причина: {response.reason}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Произошла ошибка {str(e)}")
        return None
