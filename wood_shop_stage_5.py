# === Stage 5: Связи между сущностями ===
# Project: WoodShop
from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class Product:
    name: str
    species: str
    volume: float
    status: str = "planned"


@dataclass
class Blank:
    id: str
    product_id: str
    species: str
    volume: float
    used: bool = False


class WoodShopError(Exception):
    pass


class WoodShop:
    def __init__(self):
        self._products: Dict[str, Product] = {}
        self._blanks: List[Blank] = []

    def add_product(self, product: Product) -> None:
        self._products[product.name] = product

    def add_blank(self, blank: Blank) -> None:
        self._blanks.append(blank)

    def get_blanks_for_product(self, product: Product) -> List[Blank]:
        return [b for b in self._blanks if b.product_id == product.name]

    def check_integrity(self, product: Product) -> bool:
        blanks = self.get_blanks_for_product(product)
        if not blanks:
            return False
        total_volume = sum(b.volume for b in blanks)
        if abs(total_volume - product.volume) > 0.001:
            return False
        for blank in blanks:
            if blank.species != product.species:
                return False
        return True


if __name__ == "__main__":
    shop = WoodShop()
    table = Product("Table", "Oak", 12.0)
    shop.add_product(table)
    shop.add_blank(Blank("b1", "Table", "Oak", 6.0))
    shop.add_blank(Blank("b2", "Table", "Oak", 6.0))
    print("Blanks:", len(shop.get_blanks_for_product(table)))
    print("Integrity:", shop.check_integrity(table))
    table.volume = 10.0
    print("Integrity after change:", shop.check_integrity(table))
