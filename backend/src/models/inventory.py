from .book import BookBase


class InventoryItem(BookBase):
    quantity: int
    price: float
    author: str
