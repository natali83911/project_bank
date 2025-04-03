# Project Bank

Этот проект предоставляет набор функций для работы с банковскими данными, такими как маскировка номеров карт и счетов, форматирование дат, фильтрация и сортировка данных о транзакциях.

## Описание

Проект состоит из следующих функций:

-   `get_mask_card_number(user_card_number: str) -> str`: Маскирует номер карты, показывая только первые 6 и последние 4 цифры.
-   `get_mask_account(user_account_number: str) -> str`: Маскирует номер счета, показывая только последние 4 цифры.
-   `mask_account_card(user_bank_details: str) -> str`: Обрабатывает информацию о карте или счете клиента и маскирует номер.
-   `get_date(date_string: str) -> str`: Преобразует дату в формат 'ДД.ММ.ГГГГ'.
-   `filter_by_state(list_dict_info: List[Dict], state: str = "EXECUTED") -> List[Dict]`: Фильтрует список словарей на основе указанного параметра `state`.
-   `sort_by_date(list_dict: List[Dict], reverse: bool = True) -> List[Dict]`: Сортирует список словарей на основе ключа 'date'.
-   `filter_by_currency(transactions: list[Dict[str, Any]], currency_code: str) -> Iterator[Dict[str, Any]]`: Возвращает итератор, выдающий транзакции с указанной валютой.
-   `transaction_descriptions(transactions: list[Dict[str, Any]]) -> Iterator[str]`: Возвращает итератор, выдающий описания транзакций по очереди.
-   `card_number_generator(start: int, end: int) -> Iterator[str]`: Возвращает итератор, выдающий номера банковских карт в формате `XXXX XXXX XXXX XXXX`.
-   ` log `: декоратор, который будет автоматически регистрировать детали выполнения функций, такие как время вызова, имя функции, передаваемые аргументы, результат выполнения и информация об ошибках.

## Установка

Для установки и запуска проекта необходимо выполнить следующие шаги:

1.  **Клонируйте репозиторий:**

    ```
    git clone git@github.com:natali83911/project_bank.git
    ```

2.  **Перейдите в папку проекта:**

    ```
    cd project_bank
    ```

3.  **Установите зависимости с помощью Poetry:**

    ```
    poetry install
    poetry add --group lint flake8
    poetry add --group lint mypy
    poetry add --group lint black
    poetry add --group lint isort
    poetry add --group dev pytest
    
    ```

## Использование

Примеры использования функций:

~~~

Маскировка номера карты
card_number = "6831982470375048"
masked_card = get_mask_card_number(card_number)
print(f"Masked card number: {masked_card}") # Output: 6831 98** **** 5048

Маскировка номера счета
account_number = "12345678901234567890"
masked_account = get_mask_account(account_number)
print(f"Masked account number: {masked_account}") # Output: **7890


Маскировка информации о карте/счете
bank_details = "Visa Classic 6831982470375048"
masked_details = mask_account_card(bank_details)
print(f"Masked details: {masked_details}") # Output: Visa Classic 6831 98** **** 5048


Преобразование даты
date_string = "2023-10-26T00:00:00"
formatted_date = get_date(date_string)
print(f"Formatted date: {formatted_date}") # Output: 26.10.2023


Пример данных для фильтрации и сортировки
transactions: List[Dict] = [
{"id": 1, "date": "2023-10-27T10:00:00", "state": "EXECUTED", "amount": 100},
{"id": 2, "date": "2023-10-26T12:00:00", "state": "CANCELED", "amount": 50},
{"id": 3, "date": "2023-10-28T14:00:00", "state": "EXECUTED", "amount": 200},
]

Фильтрация по статусу
executed_transactions = filter_by_state(transactions, state="EXECUTED")
print(f"Executed transactions: {executed_transactions}")


Сортировка по дате
sorted_transactions = sort_by_date(transactions)
print(f"Sorted transactions: {sorted_transactions}")


Танзакции с указанной валютой и описания транзакций по очереди.
transactions = [
{
"id": 939719570,
"state": "EXECUTED",
"date": "2018-06-30T02:08:58.425572",
"operationAmount": {
"amount": "9824.07",
"currency": {
"name": "USD",
"code": "USD"
}
},
"description": "Перевод организации",
"from": "Счет 75106830613657916952",
"to": "Счет 11776614605963066702"
}
]

for transaction in filter_by_currency(transactions, "USD"):
print(transaction)

for description in transaction_descriptions(transactions):
print(description)


Номера банковских карт в формате `XXXX XXXX XXXX XXXX`.
for card_number in card_number_generator(1, 10):
print(card_number)

декоратор функций 
@log(filename="mylog.txt")
def my_function(x, y):
    return x + y

my_function(1, 2)



~~~

## Тестирование

В проекте используются тесты, написанные с использованием `pytest`. Для запуска тестов выполните следующие шаги:

1. **Убедитесь, что установлены все зависимости (см. раздел "Установка").**
2. **Активируйте виртуальное окружение Poetry:**

~~~
    poetry env activate
    
~~~
3. **Запустите тесты с помощью команды `pytest`:**

~~~
    pytest tests
    
~~~


## Зависимости

Проект использует следующие зависимости:

*   Python 3.12.4
*   Poetry (для управления зависимостями)


## Лицензия

Этот проект лицензирован по [лицензии MIT](LICENSE).