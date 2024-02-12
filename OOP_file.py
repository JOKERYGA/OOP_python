from typing import Any


class Course:
    pass


class Module:
    pass


class LessonItem:
    def __init__(self, title: str, practices: int, duration: int) -> None:
        self.title = title
        self.practices = practices
        self.duration = duration

    def __setattr__(self, name, value: Any) -> None:
        if name == 'title' and not isinstance(value, str):
            raise TypeError("Неверный тип присваиваемых данных.")
        elif name in ('practices', 'duration'):
            if not isinstance(value, int):
                raise TypeError("Неверный тип присваиваемых данных.")
        object.__setattr__(self, name, value)
    
    def __getattr__(self, name) -> Any:
        return False

    def __delattr__(self, name: str) -> None:
        if name in ('title', 'practices', 'duration'):
            raise AttributeError("Запрещено удалять атрибуты title, practices и duration.")
        object.__delattr__(self, name)
        
pt1 = LessonItem("gdff",5,6)
print(pt1.a)