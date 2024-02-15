import math


class RadiusVector:
    def __init__(self, *args) -> None:
        if len(args) == 1:
            self.coordinates = [0] * args[0]
        else:
            self.coordinates = list(args)

    def set_coords(self, *args):
        for ind in range(len(args)):
            if ind < len(self.coordinates):
                self.coordinates[ind] = args[ind]
    
    def get_coords(self):
        return tuple(self.coordinates)
    
    def __len__(self):
        return len(self.coordinates)
    
    def __abs__(self):
        sum_of_squares = sum(coord ** 2 for coord in self.coordinates)
        return math.sqrt(sum_of_squares)


vector3D = RadiusVector(3)
vector3D.set_coords(3, -5.6, 8)
a, b, c = vector3D.get_coords()
vector3D.set_coords(3, -5.6, 8, 10, 11) # ошибки быть не должно, последние две координаты игнорируются
vector3D.set_coords(1, 2) # ошибки быть не должно, меняются только первые две координаты
res_len = len(vector3D) # res_len = 3
res_abs = abs(vector3D)