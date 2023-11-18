# 1.5
# Podvig 2
# class Money:
#     def __init__(self, x):
#         self.money = x
#
#
# my_money = Money(100)
# your_money = Money(1000)
#
# print(my_money.__dict__)
#
# Podvig 3
#
# class Point:
#     def __init__(self, x, y, color='black'):
#         self.x = x
#         self.y = y
#         self.color = color
#
#
#
# points = []
# first = 1
# second = 1
#
# for p in range(1, 1001):
#     if p == 2:
#         p = Point(first, second, "yellow")
#         points.append(p)
#     else:
#         p = Point(first, second)
#         points.append(p)
#
#     first += 2
#     second += 2
# print(points[1].__dict__)
#
# Podvig 4
#
# import random
#
#
# class Line:
#     def __init__(self, a, b, c, d):
#         self.sp = a, b
#         self.ep = c, d
#
#
# class Rect:
#     def __init__(self, a, b, c, d):
#         self.sp = a, b
#         self.ep = c, d
#
#
# class Ellipse:
#     def __init__(self, a, b, c, d):
#         self.sp = a, b
#         self.ep = c, d
#
#
# elements = []
#
# lst_classes = [Line, Rect, Ellipse]
#
# for g in range(217):
#     el = random.choice(lst_classes)(random.randint(1, 100000), random.randint(1, 100000), random.randint(1, 100000),
#                                     random.randint(1, 100000))
#     elements.append(el)
#
# for obj in elements:
#     if type(obj) == Line:
#         obj.sp = obj.ep = (0, 0)
#
# PODVIG 5
#
#
#
# class TriangleChecker:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def is_triangle(self):
#         if not all(map(lambda x: type(x) in (int, float), (self.a, self.b, self.c))):
#             return 1
#         if not all(map(lambda x: x > 0, (self.a, self.b, self.c))):
#             return 1
#         if self.a + self.b <= self.c or self.b + self.c <= self.a or self.c + self.a <= self.b:
#             return 2
#         return 3
#
# a, b, c = map(int, input().split())
# tr = TriangleChecker(a,b,c)
# print(tr.is_triangle())
#
# PODVIG 6
#
# class Graph:
#     def __init__(self, data, is_show=True):
#         self.data = data.copy()
#         self.is_show = is_show
#
#     def set_data(self, data):
#         self.data = data
#
#     def show_table(self):
#         if self.is_show is False:
#             print("Отображение данных закрыто")
#         else:
#             print(' '.join(map(str, self.data)))
#
#     def show_graph(self):
#         if self.is_show is False:
#             print("Отображение данных закрыто")
#         else:
#             print(f"Графическое отображение данных: {' '.join(map(str, self.data))}")
#
#     def show_bar(self):
#         if self.is_show is False:
#             print("Отображение данных закрыто")
#         else:
#             print(f"Столбчатая диаграмма: {' '.join(map(str, self.data))}")
#
#     def set_show(self, fl_show):
#         self.is_show = fl_show
#
#
# data_graph = list(map(int, input().split()))
# gr = Graph(data_graph)
# gr.show_bar()
# gr.set_show(fl_show=False)
# gr.show_table()

# PODVIG 7

# class CPU:
#     def __init__(self, name, fr):
#         self.name = name
#         self.fr = fr
#
#
# class Memory:
#     def __init__(self, name, volume):
#         self.name = name
#         self.volume = volume
#
#
# class MotherBoard:
#     def __init__(self, name, cpu, mem_slots, total_mem_slots=4):
#         self.name = name
#         self.cpu = cpu
#         self.mem_slots = mem_slots
#         self.total_mem_slots = total_mem_slots
#
#     def get_config(self):
#         return [f"Материнская плата: {self.name}",
#                 f"Центральный процессор: {self.cpu.name}, {self.cpu.fr}",
#                 f"Слотов памяти: {self.total_mem_slots}",
#                 f"Память: {'; '.join([f'{i.name} - {i.volume}' for i in self.mem_slots])}"]
#
#
# cpu = CPU('intel', 1333)
# mem1 = Memory("kingston", "4000")
# mem2 = Memory("kingston", "4000")
# mb = MotherBoard("aser", cpu, [mem1, mem2])

# PODVIG 8

# class Cart:
#     def __init__(self):
#         self.goods = []
#
#     def add(self, gd):
#         self.goods.append(gd)
#
#     def remove(self, indx):
#         self.goods.pop(indx)
#
#     def get_list(self):
#         return [f"{x.name}: {x.price}" for x in self.goods]
#
#
#
# class Table:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#
# class TV:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#
# class Notebook:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#
# class Cup:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
# tv1 = TV('Toshiba', 20000)
# tv2 = TV("sumsung", 50000)
# table1 = Table("kamod", 10)
# cup1 = Cup('kizaru', 100000)
#
# cart = Cart()
# cart.add(tv1)
# cart.add(tv2)
# cart.add(table1)
# cart.add(cup1)
# print(cart.get_list())


class Cell:
    def __init__(self, around_mines, mine, fl_open=False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = fl_open


class GamePole:
    def __init__(self,N,M):
        self.N = [0 * N] * N