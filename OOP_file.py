import re

class WordString:
    def __init__(self, string="") -> None:
        self.__string = string

    @property
    def string(self):
        return self.__string

    @string.setter
    def string(self, value):
        # При установке значения свойства string
        # производим преобразование строки в список слов
        self.__string = value

    def __str__(self) -> str:
        return self.__string

    def __len__(self):
        # Преобразуем строку в список слов и возвращаем его длину
        return len(re.findall(r'\b\w+\b', self.__string))

    def __call__(self, index):
        words = re.findall(r'\b\w+\b', self.__string)
        if 0 <= index < len(words):
            return words[index]
        else:
            raise IndexError("Индекс выходит за пределы списка слов")

words = WordString()
words.string = "Курс по Python ООП"
n = len(words)
first = "" if n == 0 else words(0)
print(words.string)
print(f"Число слов: {n}; первое слово: {first}")