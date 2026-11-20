# === Stage 9: Теги ===
# Project: WoodShop
from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class WoodItem:
    name: str
    species: str
    volume: float
    status: str = "draft"
    tags: List[str] = field(default_factory=list)

    def add_tag(self, tag: str) -> None:
        if tag and tag not in self.tags:
            self.tags.append(tag)

    def remove_tag(self, tag: str) -> bool:
        if tag in self.tags:
            self.tags.remove(tag)
            return True
        return False

    def has_tag(self, tag: str) -> bool:
        return tag in self.tags

    def tags(self) -> List[str]:
        return list(self.tags)

    def tag_count(self) -> int:
        return len(self.tags)


def search_by_tag(items: List[WoodItem], tag: str) -> List[WoodItem]:
    return [item for item in items if item.has_tag(tag)]


def move_tag(item: WoodItem, tag: str, position: int) -> bool:
    if tag not in item.tags:
        return False
    item.tags.remove(tag)
    if 0 <= position < len(item.tags):
        item.tags.insert(position, tag)
        return True
    return False


def sort_by_tags(items: List[WoodItem], reverse: bool = False) -> List[WoodItem]:
    return sorted(items, key=lambda item: item.tags, reverse=reverse)
