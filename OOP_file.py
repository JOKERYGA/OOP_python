from typing import Any
from math import sqrt


class Complex:
    def __init__(self, real, img) -> None:
        self.real = real
        self.img = img
    
    @staticmethod
    def correct_val(value):
        if type(value) not in (int, float):
            raise ValueError("Неверный тип данных.")
    
    @property
    def real(self):
        return self._real
    
    @real.setter
    def real(self, value):
        if isinstance(value, (int, float)):
            self._real = value
        else:
            raise ValueError("Неверный тип данных для действительной части.")
        
    @property
    def img(self):
        return self._img
    
    @img.setter
    def img(self, value):
        if isinstance(value, (int, float)):
            self._img = value
        else:
            raise ValueError("Неверный тип данных для мнимой части.")
    
    def __abs__(self):
        return sqrt(self.real**2 + self.img**2)


# Создание объекта класса Complex
cmp = Complex(7, 8)

# Установка новых значений для real и img через экземпляр класса
cmp.real = 3
cmp.img = 4

# Вычисление модуля полученного комплексного числа
c_abs = abs(cmp)
print(c_abs)
