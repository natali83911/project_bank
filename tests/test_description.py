from src.description import count_transactions_by_category, search_transactions


def test_search_transactions() -> None:
    transactions = [
        {"id": 1, "description": "Оплата ЖКХ"},
        {"id": 2, "description": "Перевод другу"},
        {"id": 3, "description": "Покупка продуктов"},
        {"id": 4},  # Без описания
    ]

    # Тест 1: Поиск существующего слова
    result = search_transactions(transactions, r"оплата")
    assert len(result) == 1, f"Ожидалось 1 совпадение, получено {len(result)}"
    assert result[0]["id"] == 1, "Найден неверный элемент"

    # Тест 2: Поиск с учетом регистра
    result = search_transactions(transactions, r"ПЕРЕВОД")
    assert len(result) == 1, "Поиск должен быть регистронезависимым"

    # Тест 3: Поиск отсутствующего слова
    result = search_transactions(transactions, r"кредит")
    assert not result, "При отсутствии совпадений должен возвращаться пустой список"


def test_count_transactions_by_category() -> None:
    transactions = [
        {"description": "Оплата коммунальных услуг"},
        {"description": "Перевод на карту"},
        {"description": "Покупка в магазине"},
        {"description": "Оплата мобильной связи"},
        {},  # Без описания
    ]
    categories = ["оплата", "перевод", "покупка", "кредит"]

    # Тест 1: Стандартный случай
    counts = count_transactions_by_category(transactions, categories)
    assert counts == {"оплата": 2, "перевод": 1, "покупка": 1, "кредит": 0}, f"Некорректный подсчет: {counts}"

    # Тест 2: Пустые входные данные
    assert count_transactions_by_category([], categories) == {k: 0 for k in categories}
    assert count_transactions_by_category(transactions, []) == {}

    # Тест 3: Разный регистр категорий
    counts = count_transactions_by_category(transactions, ["ОПЛАТА", "Перевод", "ПоКуПка"])
    assert counts["ОПЛАТА"] == 2, "Должен игнорировать регистр категорий"
