# === Stage 7: Сортировка записей ===
# Project: WoodShop
import datetime


class Product:
    def __init__(self, name, species, volume, created_at=None):
        self.name = name
        self.species = species
        self.volume = volume
        self.created_at = created_at or datetime.datetime.now()

    def sort_key_name(self):
        return self.name.lower()

    def sort_key_date(self):
        return self.created_at

    def __repr__(self):
        return "Product(name=%r, created_at=%r)" % (self.name, self.created_at)


def sort_products_by_name(products, descending=False):
    return sorted(products, key=lambda p: p.sort_key_name(), reverse=descending)


def sort_products_by_date(products, descending=False):
    return sorted(products, key=lambda p: p.sort_key_date(), reverse=descending)


if __name__ == "__main__":
    items = [
        Product("Тумба", "Дуб", 1200, datetime.datetime(2024, 1, 15)),
        Product("Стол", "Ясень", 3500, datetime.datetime(2023, 11, 2)),
        Product("Стул", "Берёза", 800, datetime.datetime(2024, 3, 20)),
    ]

    print("По названию (возрастание):")
    for p in sort_products_by_name(items, descending=False):
        print(" ", p)

    print("По названию (убывание):")
    for p in sort_products_by_name(items, descending=True):
        print(" ", p)

    print("По дате (возрастание):")
    for p in sort_products_by_date(items, descending=False):
        print(" ", p)

    print("По дате (убывание):")
    for p in sort_products_by_date(items, descending=True):
        print(" ", p)
