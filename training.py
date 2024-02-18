class ListInteger(list):
    def __init__(self, iterable=None):
        if iterable is not None:
            for item in iterable:
                if not isinstance(item, int):
                    raise TypeError("можно передавать"
                                    "только целочисленные значения")
        super().__init__(iterable)

    def __setitem__(self, index, value):
        if not isinstance(value, int):
            raise TypeError("можно передавать только целочисленные значения")
        super().__setitem__(index, value)

    def append(self, value):
        if not isinstance(value, int):
            raise TypeError("можно передавать только целочисленные значения")
        return super().append(value)
