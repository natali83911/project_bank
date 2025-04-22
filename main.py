from config import PATH_TO_CSV, PATH_TO_EXCEL, PATH_TO_JSON
from src.description import search_transactions
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.transactions import count_fin_transactions_csv, count_fin_transactions_excel
from src.utils import load_transactions_from_json
from src.widget import get_date, mask_account_card


def main():
    print(
        """
Привет! Добро пожаловать в программу работы с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла
        """
    )
    user_file = input().lower().strip()

    while True:
        if user_file == "1":
            print("Для обработки выбран JSON-файл.")
            break
        elif user_file == "2":
            print("Для обработки выбран CSV-файл.")
            break
        elif user_file == "3":
            print("Для обработки выбран XLSX-файл.")
            break
        else:
            print("Введите корректное число из предложенных вариантов.")
            break

    states = ["EXECUTED", "CANCELED", "PENDING"]

    while True:
        print(
            """
Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING.
"""
        )
        user_filter_by_state = input().upper().strip()
        if user_filter_by_state in states:
            print(f"Операции отфильтрованы по статусу {user_filter_by_state}")
            break
        else:
            print(f"Статус операции {user_filter_by_state} недоступен.")

    print("Отсортировать операции по дате? Да/Нет")
    while True:
        user_sort_by_date = input().lower().strip()
        if user_sort_by_date in ["да", "нет"]:
            break

    if user_sort_by_date == "да":
        print("Отсортировать по возрастанию или по убыванию?")
        while True:
            user_sort_by_order = input().lower().strip()
            if user_sort_by_order in ["по возрастанию", "по убыванию"]:
                break

    print("Выводить только рублевые транзакции? Да/Нет")
    while True:
        user_filter_to_rub = input().lower().strip()
        if user_filter_to_rub in ["да", "нет"]:
            break

    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    while True:
        user_search = input().lower().strip()
        if user_search in ["да", "нет"]:
            break

    transactions = []
    if user_file == "1":
        transactions = load_transactions_from_json(PATH_TO_JSON)
    elif user_file == "2":
        transactions = count_fin_transactions_csv(PATH_TO_CSV)
    elif user_file == "3":
        transactions = count_fin_transactions_excel(PATH_TO_EXCEL)

    # Фильтрация по статусу
    transactions = filter_by_state(transactions, user_filter_by_state)

    # Сортировка по дате
    if user_sort_by_date == "да":
        revers_order = user_sort_by_order == "по убыванию"
        transactions = sort_by_date(transactions, reverse=revers_order)

    # Фильтрация по валюте
    if user_filter_to_rub == "да":
        transactions = list(filter_by_currency(transactions, "RUB"))
    else:
        user_currency = (input("Введите слово для фильтрации валюты: USD, EUR: ")).upper().strip()
        transactions = list(filter_by_currency(transactions, user_currency))

    # Фильтрация по описанию
    if user_search == "да":
        search_word = (input("Введите ключевое слово для поиска: ")).lower().strip()
        transactions = search_transactions(transactions, search_word)

    print("Распечатываю итоговый список транзакций...")
    print(f"Всего банковских операций в выборке {len(transactions)}")

    for transaction in transactions:
        # Безопасное извлечение данных с проверкой ключей
        date = get_date(transaction.get("date", "Дата неизвестна"))
        description = transaction.get("description", "Описание отсутствует")
        from_account = mask_account_card(transaction.get("from", ""))  # Маскируем "откуда"
        to_account = mask_account_card(transaction.get("to", ""))  # Маскируем "куда"

        # Обработка вложенной структуры operationAmount
        operation_amount = transaction.get("operationAmount", {})
        amount = operation_amount.get("amount", "Сумма не указана")
        currency = operation_amount.get("currency", {})
        currency_code = currency.get("code", "Валюта не указана")

        # Форматированный вывод
        print(
            f"""
Дата: {date} {description}
{from_account} -> {to_account}
Сумма: {amount} {currency_code}
    """
        )


if __name__ == "__main__":
    main()
