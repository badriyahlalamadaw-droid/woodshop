# === Stage 4: Редактирование записей ===
# Project: WoodShop
def edit_product(product_id, updates, valid_fields=("name", "species", "volume", "status")):
    products = _load_products()
    target = _find(products, product_id)
    if target is None:
        raise KeyError("Изделие с таким идентификатором не существует")

    changed = {}
    for field, value in updates.items():
        if field not in valid_fields:
            raise ValueError(f"Поле '{field}' не допустимо для редактирования")
        if field not in target:
            raise ValueError(f"Поле '{field}' отсутствует в модели изделия")
        if not _is_valid_value(field, value):
            raise ValueError(f"Недопустимое значение для поля '{field}'")
        target[field] = value
        changed[field] = value

    _save(products)
    return target


def _load_products():
    try:
        with open("woodshop/products.json", "r", encoding="utf-8") as handle:
            return json.load(handle)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def _save(products):
    with open("woodshop/products.json", "w", encoding="utf-8") as handle:
        json.dump(products, handle, ensure_ascii=False, indent=2)


def _find(products, product_id):
    for product in products:
        if product.get("id") == product_id:
            return product
    return None


def _is_valid_value(field, value):
    allowed_statuses = {"new", "in_progress", "ready", "archived"}
    if field == "status" and value not in allowed_statuses:
        return False
    if field == "volume" and (not isinstance(value, (int, float)) or value <= 0):
        return False
    if field == "name" and not isinstance(value, str) or not value.strip():
        return False
    if field == "species" and not isinstance(value, str) or not value.strip():
        return False
    return True


if __name__ == "__main__":
    edited = edit_product(1, {"name": "Стул", "status": "ready"})
    print("Обновлённое изделие:", edited)
