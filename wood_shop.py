# === Stage 1: Каркас модуля ===
# Project: WoodShop
from dataclasses import dataclass, field
from typing import Optional, List


@dataclass
class Izdeliye:
    """Столярное изделие: название, порода, объём и статус."""

    name: str
    wood: str
    volume: float
    status: str = "в работе"

    def describe(self) -> str:
        return (
            f"изделие «{self.name}» — {self.wood}, "
            f"объём {self.volume} л, статус: {self.status}"
        )


def make_demo_records() -> List[Izdeliye]:
    """Создаём несколько демонстрационных записей изделия."""

    records = [
        Izdeliye("Стул", "дуб", 12.5),
        Izdeliye("Стол", "сосна", 45.0, "готов"),
        Izdeliye("Шкаф", "берёза", 210.0, "в работе"),
        Izdeliye("Полка", "ясень", 8.3, "отделка"),
    ]
    return records


def main() -> None:
    """Выводим демо-записи и краткую справку по модулю."""

    print("WoodShop: столярная мастерская")
    print("-" * 30)

    for record in make_demo_records():
        print(record.describe())

    print("-" * 30)
    print("Модуль: изделия, доски, раскрой и отделка")


if __name__ == "__main__":
    main()
