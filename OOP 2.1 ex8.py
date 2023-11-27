class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_coords(self):
        return self.__x, self.__y

    @staticmethod
    def cheacking(fl):
        if fl in (int, float):
            return True
        else:
            return False


class Rectangle:
    def __init__(self, *args):
        if len(args) == 4:
            self.__sp = args[0], args[1]
            self.__ep = args[2], args[3]
        else:
            self.__sp, self.__ep = args


    def set_coords(self, sp, ep):
        self.__sp = sp
        self.__ep = ep

    def get_coords(self):
        return self.__sp, self.__ep

    def draw(self):
        print(f"Прямоугольник с координатами: {self.__sp}, {self.__ep}")


rect = Rectangle((0, 0), (20, 34))
