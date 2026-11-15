# === Stage 6: Генерация идентификаторов ===
# Project: WoodShop
"""WoodShop/ids.py — генерация уникальных идентификаторов с префиксом проекта.

Создаёт идентификаторы вида "WOODSHOP_<счётчик>" и проверяет их на
уникальность относительно уже существующих значений. Работает только со
стандартной библиотекой и не ссылается на другой код проекта.
"""

PROJECT_PREFIX = "WOODSHOP"
_COUNTER = 0


def generate_unique_id(existing: set) -> str:
    """Генерирует уникальный идентификатор и добавляет его в набор.

    existing — mutable-контейнер уже занятых идентификаторов. Возвращаемое
    значение сразу добавляется в этот контейнер, чтобы избежать повторной
    проверки одного и того же значения.
    """
    global _COUNTER
    while True:
        _COUNTER += 1
        candidate = f"{PROJECT_PREFIX}_{_COUNTER}"
        if candidate not in existing:
            existing.add(candidate)
            return candidate


def generate_unique_id_safe(existing: set) -> str:
    """Генерирует уникальный идентификатор без модификации переданного набора.

    Полезно, когда нужно только проверить доступность значения, не
    изменяя передаваемый коллектор.
    """
    global _COUNTER
    while True:
        _COUNTER += 1
        candidate = f"{PROJECT_PREFIX}_{_COUNTER}"
        if candidate not in existing:
            return candidate


if __name__ == "__main__":
    used = set()
    first = generate_unique_id(used)
    print("Первый сгенерированный:", first)
    print("Занятых идентификаторов:", len(used))
