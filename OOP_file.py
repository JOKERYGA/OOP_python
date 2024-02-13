class Museum:
    def __init__(self, name) -> None:
        self.name = name
        self.exhibits = []
        
    def add_exhibit(self, obj):
        self.exhibits.append(obj)

    def remove_exhibit(self, obj):
        self.exhibits.remove(obj)

    def get_info_exhibit(self, indx):
        if 0 <= indx <= len(self.exhibits) - 1:
            class_instance = self.exhibits[indx]
            return f"Описание экспоната {class_instance.name}: {class_instance.descr}"
                

class Picture:
    def __init__(self, name, author, descr):
        self.name = name
        self.author = author
        self.descr = descr


class Mummies:
    def __init__(self, name, location, descr):
        self.name = name
        self.location = location
        self.descr = descr


class Papyri:
    def __init__(self, name, date, descr):
        self.name = name
        self.date = date
        self.descr = descr