# === Stage 10: Группировка ===
# Project: WoodShop
from collections import Counter


def group_by_species(items):
    counts = Counter()

    for item in items:
        species = item.get("species")
        counts[species] += 1

    return counts


def grouped_with_counts(items):
    grouped = {}

    for item in items:
        species = item.get("species")
        grouped.setdefault(species, []).append(item)

    result = {}

    for species, group in grouped.items():
        result[species] = {
            "items": group,
            "count": len(group),
        }

    return result


def print_report(items):
    print("Группировка изделий по породе:")
    print("-" * 40)

    grouped = grouped_with_counts(items)

    if not grouped:
        print("Нет данных.")
        return

    for species, data in sorted(grouped.items()):
        print(f"{species}: {data['count']} шт.")


if __name__ == "__main__":
    sample = [
        {"id": 1, "name": "Стул", "species": "дуб", "status": "готов"},
        {"id": 2, "name": "Стол", "species": "ясень", "status": "в работе"},
        {"id": 3, "name": "Стул", "species": "дуб", "status": "готов"},
        {"id": 4, "name": "Полка", "species": "сосна", "status": "готов"},
    ]

    report = group_by_species(sample)
    print(report)

    print_report(sample)
