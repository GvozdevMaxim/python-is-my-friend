# import sys
#
#
# # здесь объявляется класс StreamData
# class StreamData:
#     def create(self, fields, lst_values):
#         if len(fields) != len(lst_values):
#             return False
#         else:
#             for i, x in enumerate(fields):
#                 setattr(self, x, lst_values[i])
#             return True
#
#
# class StreamReader:
#     FIELDS = ('id', 'title', 'pages')
#
#     def readlines(self):
#         lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
#         sd = StreamData()
#         res = sd.create(self.FIELDS, lst_in)
#         return sd, res
#
#
# sr = StreamReader()
# data, result = sr.readlines()

# 9
# import sys
#
# # программу не менять, только добавить два метода
# lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
#
#
# class DataBase:
#     lst_data = []
#     FIELDS = ('id', 'name', 'old', 'salary')
#     def insert(self, data):
#         for row in data:
#             gen = {self.FIELDS[i]: x for i, x in enumerate(row.split(' '))}
#             self.lst_data.append(gen)
#
#     def select(self, a, b):
#         # if b > len(self.lst_data):
#         #     b = len(self.lst_data)
#         res = self.lst_data[a:b + 1]
#         return res
#
#     # здесь добавлять методы
#
#
# db = DataBase()
# db.insert(lst_in)

class Translator:
    def add(self, eng, rus):
        if 'tr' not in self.__dict__:
            self.tr = {}
        self.tr.setdefault(eng, [])
        temp = self.tr.get(eng)
        if rus not in temp:
            temp.append(rus)

# здесь продолжайте метод add
    def remove(self, eng):
        if hasattr(self.tr, eng):
            self.tr.pop(eng)

# здесь продолжайте метод remove

    def translate(self, eng):
        return self.tr.get(eng)
# здесь продолжайте метод translate


# здесь создавайте объект класса Translator
tr = Translator()

tr.add("tree", "дерево")
tr.add("car", "машина")
tr.add("car", "автомобиль")
tr.add("leaf", "лист")
tr.add("river", "река")
tr.add("go", "идти")
tr.add("go", "ехать")
tr.add("go", "ходить")
tr.add("milk", "молоко")
tr.remove("car")
print(' '.join(tr.translate("go")))