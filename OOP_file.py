from typing import Any


class Course:
    def __init__(self, name) -> None:
        self.name = name
        self.modules = []

    def add_module(self, module):
        self.modules.append(module)

    def remove_module(self, indx):
        if 0 <= indx <= len(self.modules) - 1:
            self.modules.pop(indx)


class Module:
    def __init__(self, name) -> None:
        self.name = name
        self.lessons = []

    def add_lesson(self, lesson):
        self.lessons.append(lesson)

    def remove_lesson(self, indx):
        if 0 <= indx <= len(self.lessons) - 1:
            self.lessons.pop(indx)


class LessonItem:
    def __init__(self, title: str, practices: int, duration: int) -> None:
        self.title = title
        self.practices = practices
        self.duration = duration

    def __setattr__(self, name, value: Any) -> None:
        if name == 'title' and not isinstance(value, str):
            raise TypeError("Неверный тип присваиваемых данных для 'title'.")
        elif name in ('practices', 'duration') and not isinstance(value, int):
            raise TypeError(f"Неверный тип присваиваемых данных для '{name}'.")
        elif name in ('practices', 'duration') and value < 0:
            raise ValueError(f"Значение атрибута '{name}' не может быть отрицательным.")
        else:
            object.__setattr__(self, name, value)

    def __getattr__(self, name) -> Any:
        return False

    def __delattr__(self, name: str) -> None:
        if name in ('title', 'practices', 'duration'):
            raise AttributeError("Запрещено удалять атрибуты title, practices и duration.")
        object.__delattr__(self, name)


course = Course("Python ООП")
module_1 = Module("Часть первая")
module_1.add_lesson(LessonItem("Урок 1", 7, 1000))
module_1.add_lesson(LessonItem("Урок 2", 10, 1200))
module_1.add_lesson(LessonItem("Урок 3", 5, 800))
course.add_module(module_1)
module_2 = Module("Часть вторая")
module_2.add_lesson(LessonItem("Урок 1", 7, 1000))
module_2.add_lesson(LessonItem("Урок 2", 10, 1200))
course.add_module(module_2)
print(module_2.__dict__)