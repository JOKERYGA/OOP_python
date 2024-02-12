from typing import Any


class Shop:
    def __init__(self, name) -> None:
        self.name = name
        self.goods = []

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)


class Product:
    def __init__(self, name, weight: int, price: int) -> None:
        self.name = name
        self.id = id(self)
        if weight < 0 or price < 0:
            raise TypeError("Неверный тип присваиваемых данных.")
        else:
            self.weight = weight
            self.price = price

    def __setattr__(self, name: str, value) -> None:
        if name == 'name' and not isinstance(value, str):
            raise TypeError("Неверный тип присваиваемых данных.")
        elif name == 'weight' and not type(value) in (int, float) and value < 0:
            raise TypeError("Неверный тип присваиваемых данных.")
        elif name == 'price' and not type(value) in (int, float) and value < 0:
            raise TypeError("Неверный тип присваиваемых данных.")
        elif name == 'id' and not isinstance(value, int):
            raise TypeError("Неверный тип присваиваемых данных.")
        else:
            object.__setattr__(self, name, value)

    def __delattr__(self, name: str) -> None:
        if name == "id":
            raise AttributeError("Атрибут id удалять запрещено.")