class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 10000

    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def __ge__(self, other):
        if not isinstance(other, Dimensions):
            raise TypeError("Правый оперант долэжен быть объектом DIM")
        return self.__a * self.__b * self.__c >= other.__a * other.__b * other.__c

    def __gt__(self, other):
        if not isinstance(other, Dimensions):
            raise TypeError("Правый оперант долэжен быть объектом DIM")
        return self.__a * self.__b * self.__c > other.__a * other.__b * other.__c

    def __lt__(self, other):
        if not isinstance(other, Dimensions):
            raise TypeError("Правый оперант долэжен быть объектом DIM")
        return self.__a * self.__b * self.__c < other.__a * other.__b * other.__c

    def __le__(self, other):
        if not isinstance(other, Dimensions):
            raise TypeError("Правый оперант долэжен быть объектом DIM")
        return self.__a * self.__b * self.__c <= other.__a * other.__b * other.__c

    @classmethod
    def min_max(cls, value):
        return cls.MIN_DIMENSION <= value <= cls.MAX_DIMENSION

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, new_value):
        if self.min_max(new_value):
            self.__a = new_value

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, new_value):
        if self.min_max(new_value):
            self.__b = new_value

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, new_value):
        if self.min_max(new_value):
            self.__c = new_value


class ShopItem:
    def __init__(self, name, price, dim):
        self.name = name
        self.price = price
        self.dim = dim


item1 = ShopItem("кеды", 1024, (40, 30, 120))
item2 = ShopItem("зонт", 500.24, (10, 20, 50))
item3 = ShopItem("холодильник", 40000, (2000, 600, 500))
item4 = ShopItem("табуретка", 2000.99, (500, 200, 200))
lst_shop = [item1, item2, item3, item4]

lst_shop_sorted = sorted(lst_shop, key=lambda x: x.dim)
