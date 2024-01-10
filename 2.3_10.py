class PolyLine:
    def __init__(self, *args):
        arguments = list(args)
        self.__cooeds = arguments

    def add_coord(self, x, y):
        self.__cooeds.append((x, y))

    def remove_coord(self, indx):
        self.__cooeds.pop(indx)

    def get_coords(self):
        return self.__cooeds

poly = PolyLine((1, 2), (3, 5), (0, 10), (-1, 8))
poly.add_coord(1,3)
poly.remove_coord(1)
poly.get_coords()