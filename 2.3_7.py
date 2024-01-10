from math import sqrt


class RadiusVector:
    def __init__(self, *args):
        self.arguments = args
        if len(self.arguments) == 1:
            self.coords = self.arguments[0] * [0]
        else:
            self.coords = [*self.arguments]

    def get_coords(self):
        return tuple(self.coords)

    def set_coords(self, *args):
        n = min(len(args), len(args))
        self.coords[:n] = args

    def __len__(self):
        return len(self.coords)

    def __abs__(self):
        temp = 0
        for i in range(len(self.coords)):
            temp += self.coords[i] * self.coords[i]
        return sqrt(temp)


vector3D = RadiusVector(3)
vector3D.set_coords(3, -5.6, 8)
a, b, c = vector3D.get_coords()
vector3D.set_coords(3, -5.6, 8, 10, 11)  # ошибки быть не должно, последние две координаты игнорируются
vector3D.set_coords(1, 2)  # ошибки быть не должно, меняются только первые две координаты
res_len = len(vector3D)  # res_len = 3
res_abs = abs(vector3D)
