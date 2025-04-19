import re
from collections import Counter
from typing import Dict, List


def search_transactions(transactions: List[Dict], search_str: str) -> List[Dict]:
    """Фильтрует список операций, возвращая только те словари,
    у которых в поле 'description' есть совпадение с search_str (регулярное выражение)."""

    pattern = re.compile(search_str, re.IGNORECASE)  # игнорируем регистр для удобства поиска
    filtered = [tran for tran in transactions if "description" in tran and pattern.search(tran["description"])]
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
