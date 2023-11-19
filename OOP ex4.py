# PODVIG 6

# class AbstractClass:
#     def __new__(cls, *args, **kwargs):
#         return "Ошибка: нельзя создавать объекты абстрактного класса"
#
#
# obj = AbstractClass()

# PODVIG 7

# class SingletonFive:
#     i = 0
#     __instance = None
#     def __new__(cls, *args, **kwargs):
#         if cls.i < 4:
#
#             cls.__instance = super().__new__(cls)
#             print(id(super().__new__(cls)))
#         else:
#             print(id(cls.__instance))
#             return cls.__instance
#
#
#     def __init__(self, name):
#         self.name = name
#
# res = []
# objs = [print(SingletonFive(str(n))) for n in range(10)]

# # Podvig 8
# TYPE_OS = 1 # 1 - Windows; 2 - Linux
# class DialogWindows:
#     name_class = "DialogWindows"
#
#
# class DialogLinux:
#     name_class = "DialogLinux"
#
#
# class Dialog:
#     def __new__(cls, *args, **kwargs):
#         ob = super().__new__(DialogWindows if TYPE_OS == 1 else DialogLinux)
#         setattr(ob, 'name', args[0])
#         return ob
#
#
# dlg = Dialog("<название>")
# print(dlg.__dict__)
# print(DialogWindows.__dict__)


# class Point:
#     def __init__(self, x, y):
#         Point.x = x
#         Point.y = y
#
#     def clone(self):
#         return Point(self.x, self.y)
#
#
# pt = Point(2, 3)
#
# pt_clone = Point.clone(pt)
# print(pt)
# print(pt_clone)

# Podvig 10

# class Loader:
#     def parse_format(self, string, factory):
#         seq = factory.build_sequence()
#         for sub in string.split(","):
#             item = factory.build_number(sub)
#             seq.append(item)
#
#         return seq
#
# class Factory():
#     def build_sequence(self):
#         return []
#
#     def build_number(self, string):
#         string = float(string)
#         return string
#
# ld = Loader()
# res = ld.parse_format("4, 5, -6.5", Factory())
# print(res)