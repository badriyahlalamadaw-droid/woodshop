# === Stage 11: Постраничный вывод ===
# Project: WoodShop
from dataclasses import dataclass


@dataclass
class Page:
    page: int = 1
    page_size: int = 10


def paginate(items, page: Page):
    start = (page.page - 1) * page.page_size
    return items[start:start + page.page_size], len(items) - start


def apply_page_query(items, query):
    page = Page()
    if "page" in query:
        page.page = int(query["page"])
    if "page_size" in query:
        page.page_size = int(query["page_size"])
    return paginate(items, page)
