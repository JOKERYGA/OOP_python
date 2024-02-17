import itertools


class Thing:
    id_counter = itertools.count(1)

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.id = next(Thing.id_counter)
        self.weight = None
        self.dims = None
        self.memory = None
        self.frm = None

    def get_data(self):
        return (self.id, self.name, self.price, self.weight,
                self.dims, self.memory, self.frm)


class Table(Thing):
    def __init__(self, name, price, weight, dims):
        super().__init__(name, price)
        self.weight = weight
        self.dims = dims


class ElBook(Thing):
    def __init__(self, name, price, memory, frm):
        super().__init__(name, price)
        self.memory = memory
        self.frm = frm
