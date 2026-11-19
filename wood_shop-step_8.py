# === Stage 8: Текстовый поиск ===
# Project: WoodShop
from difflib import SequenceMatcher


def highlight_matches(text: str, patterns: list[str]) -> str:
    """Подсвечивает в строке все совпадения из списка паттернов.

    Поиск без учёта регистра. Совпадения выделяются символом маркера
    (в примере используется символ подчёркивания). Строка, не содержащая
    ни одного совпадения, возвращается без изменений.
    """
    if not patterns:
        return text
    text = text.lower()
    markers = [p.lower() for p in patterns if p.lower()]
    if not markers:
        return text

    result: list[str] = []
    cursor = 0
    for pattern in markers:
        start = 0
        while True:
            index = text.find(pattern, start)
            if index == -1:
                break
            result.append(text[cursor:index])
            result.append(pattern)
            cursor = index + len(pattern)
            start = cursor
    result.append(text[cursor:])
    return "".join(result)


def find_products(products: list[dict], query: str) -> list[dict]:
    """Находит изделия по текстовым полям названия и породы.

    Поиск регистронезависимый. Для каждого найденного изделия строка
    вывода формируется с подсветкой совпадений, а само изделие добавляется
    в результат.
    """
    query = query.strip()
    if not query:
        return []

    query_lower = query.lower()
    found: list[dict] = []
    for product in products:
        if query_lower in product.get("название", "").lower():
            found.append(product)
            continue
        if query_lower in product.get("порода", "").lower():
            found.append(product)
            break

    if not found:
        return []

    output_lines = [
        highlight_matches(
            f'{product["название"]} ({product["порода"]})',
            [product["название"], product["порода"]],
        )
        for product in found
    ]
    return [{"output": line} for line in output_lines]
