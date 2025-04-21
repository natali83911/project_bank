import re
from collections import Counter
from typing import Dict, List


def search_transactions(transactions: List[Dict], search_str: str) -> List[Dict]:
    """Фильтрует список операций, возвращая только те словари,
    у которых в поле 'description' есть совпадение с search_str (регулярное выражение)."""

    filtered = []

    # Компилируем регулярное выражение с флагом IGNORECASE
    try:
        pattern = re.compile(re.escape(search_str), re.IGNORECASE)
    except re.error:
        # Если некорректный паттерн (например, незакрытые скобки)
        pattern = re.compile(re.escape(""), re.IGNORECASE)  # Пустой паттерн

    for transaction in transactions:
        try:
            description = transaction.get("description", "")

            # Ищем как подстроку в любом месте описания
            if pattern.search(description):
                filtered.append(transaction)

        except (AttributeError, KeyError):
            # Пропускаем транзакции с некорректной структурой
            continue

    return filtered


def count_transactions_by_category(transactions: List[Dict], categories: List[str]) -> Dict[str, int]:
    """Подсчитывает количество операций для каждой категории из списка, используя Counter."""

    # Собираем все категории, найденные в описаниях операций
    matched_categories = []

    for transaction in transactions:
        description = transaction.get("description", "").lower()
        for category in categories:
            if category.lower() in description:
                matched_categories.append(category)

    # Считаем вхождения с помощью Counter
    counter = Counter(matched_categories)

    # Гарантируем наличие всех категорий в результате (даже с нулевым значением)
    return {category: counter.get(category, 0) for category in categories}
