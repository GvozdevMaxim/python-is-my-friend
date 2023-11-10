# class Point:
#     color = 'yellow'
#     circls = 2
#
# print(Point.color)
# Point.circls = 2
# print(Point.circls)
#
#
# a = Point()
#
# print(a.circls)


# 1


# # 1.4
# class DataBase:
#     pk = 1
#     title = "Классы и объекты"
#     author = "Сергей Балакирев"
#     views = 14356
#     comments = 12
#
#
# # 1.5
# class Goods:
#     title = "Мороженое"
#     weight = 154
#     tp = 'Еда'
#     price = 1024
#
#
# Goods.price = 2048
# setattr(Goods, "inflation", 100)


# 1.6
# class Car:
#     pass
#
#
# setattr(Car, 'model', 'Тойота')
# setattr(Car, "color", "Розовый")
# setattr(Car, "number", "П111УУ77")
# for k, v in Car.__dict__.items():
#     if k == 'color':
#         print(v)


# 1.7
# class Notes:
#     vid = 1005435
#     title = "Шутка"
#     author = "И.С. Бах"
#     pages = 2
#
#
# print(getattr(Notes, "author"))

# 1.8
# class Dictionary:
#     rus = "Питон"
#     eng = "Python"
#
#
# print(getattr(Dictionary, "ruw_world", False))

# class TravelBlog:
#     total_blogs = 0
#
#
# tb1 = TravelBlog()
# tb1.name = "Франция"
# setattr(tb1, "days", 6)
#
# TravelBlog.total_blogs += 1
#
# tb2 = TravelBlog()
# tb2.name = "Италия"
# tb2.days = 5
#
# TravelBlog.total_blogs += 1

# 1.9
# class Figure:
#     type_fig = "ellipse"
#     color = "red"
#
#
# fig1 = Figure()
# fig1.start_pt = (10, 5)
# fig1.end_pt = (100, 20)
# fig1.color = "blue"
#
# if hasattr(fig1, "color"):
#     delattr(fig1, "color")
#
# print(*fig1.__dict__.keys())

# 1.10
# class Person:
#     name = "Сергей Балакирев"
#     job = "Программист"
#     city = "Москва"
#
# p1 = Person()
# print(True if hasattr(p1.__dict__, "job") else False)


