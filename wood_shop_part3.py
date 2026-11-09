# === Stage 3: Хранилище в памяти ===
# Project: WoodShop
import uuid


class Product:
    """Столярное изделие: название, порода, объём и статус."""

    def __init__(self, name, species, volume, status="created"):
        self.id = uuid.uuid4().hex
        self.name = name
        self.species = species
        self.volume = volume
        self.status = status

    def set_status(self, status):
        self.status = status

    def __repr__(self):
        return f"Product(id={self.id}, name={self.name}, species={self.species}, volume={self.volume}, status={self.status})"


class ProductStorage:
    """Память изделий в словаре, keyed по id."""

    def __init__(self):
        self._items = {}

    def add(self, product):
        self._items[product.id] = product
        return product

    def get(self, product_id):
        return self._items.get(product_id)

    def list(self):
        return list(self._items.values())

    def __len__(self):
        return len(self._items)
