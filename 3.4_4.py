class NewList:
    def __init__(self, lst=None):
        self._lst = lst[:] if lst and type(lst) == list else []

    def get_list(self):
        return self._lst



    def __sub__(self, other):
        if type(other) not in (list, NewList):
            raise ArithmeticError("Правый операнд должен быть типом list или объектом NewList")
        other_list = other if type(other) is list else other.get_list()
        return NewList(self.__diff_list(self._lst, other_list))

    def __rsub__(self, other):
        if type(other) != list:
            raise ArithmeticError("Правый операнд должен быть типом list или объектом NewList")
        return NewList(self.__diff_list(other, self._lst))

    @staticmethod
    def __diff_list(lst1, lst2):
        if len(lst2) == 0:
            return lst1

        temp_lst = lst2[:]
        print(list([x for x in lst1 if not NewList.__is_element(x, temp_lst)]))
        return [x for x in lst1 if not NewList.__is_element(x, temp_lst)]

    @staticmethod
    def __is_element(x, temp_lst):
        res = any(map(lambda xx: type(x) == type(xx) and x == xx, temp_lst))
        if res:
            temp_lst.remove(x)
        return res


lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
lst2 = NewList([0, 1, 2, 3, True])
res_1 = lst1 - lst2  # NewList: [-4, 6, 10, 11, 15, False]

lst1 -= lst2 # NewList: [-4, 6, 10, 11, 15, False]
res_2 = lst2 - [0, True] # NewList: [1, 2, 3]
res_3 = [1, 2, 3, 4.5] - res_2 # NewList: [4.5]
a = NewList([2, 3])
res_4 = [1, 2, 2, 3] - a # NewList: [1, 2]
