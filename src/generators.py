from typing import Any, Dict, Iterator


def filter_by_currency(transactions: list[Dict[str, Any]], currency_code: str) -> Iterator[Dict[str, Any]]:
    """
    Возвращает итератор, выдающий транзакции с указанной валютой.
    """
    for transaction in transactions:
        try:
            if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency_code:
                yield transaction
        except AttributeError:
            continue


def transaction_descriptions(transactions: list[Dict[str, Any]]) -> Iterator[str]:
    """
    Возвращает итератор, выдающий описания транзакций по очереди.
    """
    for transaction in transactions:
        yield transaction.get("description")


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """
    Возвращает итератор, выдающий номера банковских карт в формате XXXX XXXX XXXX XXXX.

    """
    if start > end:
        raise ValueError("Начальное значение должно быть меньше или равно конечному")
    for number in range(start, end + 1):
        formatted_number = "{:016d}".format(number)
        yield "{} {} {} {}".format(
            formatted_number[:4], formatted_number[4:8], formatted_number[8:12], formatted_number[12:]
        )
