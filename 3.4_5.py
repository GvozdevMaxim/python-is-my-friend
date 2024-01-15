class ListMath:
    def __init__(self, lst=None):
        self.lst = list()
        if lst:
            self.lst = self.check_type(lst)
        self.lst_math = self.lst.copy()

    @staticmethod
    def check_type(lst):
        return [x for x in lst if type(x) in (int, float)]

    def get_lst(self):
        return self.lst_math

    def __add__(self, other):
        if type(other) not in (int, float):
            raise ArithmeticError("Правый операнд должен быть типом int или float")
        return ListMath(self.__plus(self.lst_math, other))

    def __radd__(self, other):
        return self + other
    @staticmethod
    def __plus(lst, other):
        return [x + other for x in lst]

    @staticmethod
    def __plus_invert(other, lst):
        return [x + other for x in lst]

    def __sub__(self, other):
        if type(other) not in (int, float, ListMath):
            raise ArithmeticError("Правый операнд должен быть типом int, float или ListMach")
        return ListMath(self.__minus(self.lst_math, other))

    def __rsub__(self, other):
        if type(other) not in (int, float):
            raise ArithmeticError("Правый операнд должен быть типом int или float")
        return ListMath(self.__minus_invert(other, self.lst_math))

    def __isub__(self, other):
        if type(other) not in (int, float, ListMath):
            raise ArithmeticError("Правый операнд должен быть типом int или float или ListMath")
        self.__minus(self.lst_math, other)
        return self

    @staticmethod
    def __minus(lst, other):
        return [x - other for x in lst]

    @staticmethod
    def __minus_invert(other, lst):
        return [other - x for x in lst]

    def __mul__(self, other):
        if type(other) not in (int, float, ListMath):
            raise ArithmeticError("Правый операнд должен быть типом int, float или ListMach")
        return ListMath(self.__multiply(self.lst_math, other))

    def __rmul__(self, other):
        if type(other) not in (int, float):
            raise ArithmeticError("Правый операнд должен быть типом int или float")
        return ListMath(self.__multiply_invert(other, self.lst_math))

    def __imul__(self, other):
        if type(other) not in (int, float, ListMath):
            raise ArithmeticError("Правый операнд должен быть типом int или float или ListMath")
        self.__multiply(self.lst_math, other)
        return self

    @staticmethod
    def __multiply(lst, other):
        return [x * other for x in lst]

    @staticmethod
    def __multiply_invert(other, lst):
        return [x * other for x in lst]

    def __truediv__(self, other):
        if type(other) not in (int, float, ListMath):
            raise ArithmeticError("Правый операнд должен быть типом int, float или ListMach")
        return ListMath(self.__delenie(self.lst_math, other))

    def __rtruediv__(self, other):
        if type(other) not in (int, float):
            raise ArithmeticError("Правый операнд должен быть типом int или float")
        return ListMath(self.__delenie_invert(other, self.lst_math))

    def __itruediv__(self, other):
        if type(other) not in (int, float, ListMath):
            raise ArithmeticError("Правый операнд должен быть типом int или float или ListMath")
        self.__delenie(self.lst_math, other)
        return self

    @staticmethod
    def __delenie(lst, other):
        return [x / other for x in lst]

    @staticmethod
    def __delenie_invert(other, lst):
        return [other / x for x in lst]


lst = ListMath([1,2,3])  # ListMath: [1, -5, 7.68]
print(f"Исходный масив {lst.__dict__}")
lst = lst + 76  # сложение каждого числа списка с определенным числом
print(f"Первое сложение {lst.__dict__}, ")
lst = 6.5 + lst  # сложение каждого числа списка с определенным числом
print(f"Второе сложение {lst.__dict__}")
lst += 76.7  # сложение каждого числа списка с определенным числом
print(f"Третье сложение {lst.__dict__}")
lst = lst - 76  # вычитание из каждого числа списка определенного числа
print(f"Первое вычитание {lst.__dict__}")
lst = 7.0 - lst  # вычитание из числа каждого числа списка
print(f"Второе вычитание {lst.__dict__}")
lst -= 76.3
print(f"Третье вычитание {lst}")
lst = lst * 5 # умножение каждого числа списка на указанное число (в данном случае на 5)
print(f"Первое умножение {lst.__dict__}")
lst = 5 * lst # умножение каждого числа списка на указанное число (в данном случае на 5)
print(f"Второе умножение {lst.__dict__}")
lst *= 5.54
print(f"Третье умножение {lst}")
lst = lst / 13 # деление каждого числа списка на указанное число (в данном случае на 13)
print(f"Первое деление {lst.__dict__}")
lst = 3 / lst # деление числа на каждый элемент списка
print(f"Второе деление {lst.__dict__}")
lst /= 13.0
print(f"Третье деление {lst}")
