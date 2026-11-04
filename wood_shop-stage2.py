# === Stage 2: Проверка полей ===
# Project: WoodShop
def normalize_name(raw):
    text = (raw or "").strip()
    if not text:
        raise ValueError("Название не может быть пустым")
    if len(text) > 120:
        raise ValueError("Название слишком длинное (максимум 120 символов)")
    cleaned = " ".join(text.split())
    if not cleaned:
        raise ValueError("Название не может быть пустым")
    return cleaned


def validate_species(raw):
    text = (raw or "").strip()
    if not text:
        raise ValueError("Порода древесины обязательна для заполнения")
    if len(text) > 60:
        raise ValueError("Слишком длинное название породы")
    if "  " in text:
        raise ValueError("Порода содержит двойной пробел")
    return text


def validate_volume(raw):
    text = (raw or "").strip()
    try:
        value = float(text)
    except (TypeError, ValueError):
        raise ValueError("Объём должен быть числом, например 0.5")
    if value != value:
        raise ValueError("Объём не может быть некорректным значением")
    if value <= 0:
        raise ValueError("Объём должен быть больше нуля")
    if value > 100000:
        raise ValueError("Объём превышает разумный предел (максимум 100000)")
    return value


def validate_status(raw, allowed):
    text = (raw or "").strip()
    if not text:
        raise ValueError("Статус изделия обязателен")
    normalized = text.lower()
    if normalized not in [item.lower() for item in allowed]:
        raise ValueError(
            f"Недопустимый статус. Допустимые значения: "
            + ", ".join(allowed)
        )
    return normalized


def validate_product(raw_name, raw_species, raw_volume, raw_status, allowed_status):
    name = normalize_name(raw_name)
    species = validate_species(raw_species)
    volume = validate_volume(raw_volume)
    status = validate_status(raw_status, allowed_status)
    return name, species, volume, status
