from app.base import BaseStorage


class Store(BaseStorage):
    """Класс склад"""
    def __init__(self, items: dict, capacity=100):
        super().__init__(items, capacity)
