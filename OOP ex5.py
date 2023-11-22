# class Coords:
#     MIN_COORS = 0
#     MAX_COORDS = 100
#
#     @classmethod
#     def validate(cls, agr):
#         return cls.MIN_COORS <= agr  <= cls.MAX_COORDS
#
#     def __init__(self, x, y, z):
#         self.x = 0
#         self.y = 0
#         self.z = 0
#         if self.validate(x) and self.validate(y) and self.validate(z):
#             self.x = x
#             self.y = y
#             self.z = z
#
#
#     def get_max(self):
#         return max(self.x, self.y, self.z)
#
#
# ball_coordinate = Coords(5, 3, 13)
# print(ball_coordinate.__dict__)
# max_coords = Coords.get_max(ball_coordinate)
# print(max_coords)
#
# PODVIG 6
#
# class Factory:
#     @classmethod
#     def build_sequence(cls):
#         return []
#     @classmethod
#     def build_number(cls, string):
#         return int(string)
# class Loader:
#     @staticmethod
#     def parse_format(string, factory):
#         seq = factory.build_sequence()
#         for sub in string.split(","):
#             item = factory.build_number(sub)
#             seq.append(item)
#
#         return seq
#
#
# # эти строчки не менять!
# res = Loader.parse_format("1, 2, 3, -5, 10", Factory)
# print(res)
#
# PODVIG 7
#
# from string import ascii_lowercase, digits
#
#
# class TextInput:
#     def __init__(self, name, size=10):
#         if self.check_name(name):
#             self.login = name
#             self.size = int(size)
#         else:
#             raise ValueError("некорректное поле name")
#
#     CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
#     CHARS_CORRECT = CHARS + CHARS.upper() + digits
#
#     @classmethod
#     def check_name(cls, name):
#         for i, s in enumerate(name):
#             if 3 <= len(name) <= 50:
#                 if s in cls.CHARS_CORRECT:
#                     return True
#                 else:
#                     raise ValueError("некорректное поле name")
#
#     def get_html(self):
#         return f"<p class='login'>{self.login}: <input type='text' size={self.size} />"
#
#
# class PasswordInput:
#     CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
#     CHARS_CORRECT = CHARS + CHARS.upper() + digits
#
#     @classmethod
#     def check_name(cls, name):
#         for i, s in enumerate(name):
#             if 3 <= len(name) <= 50:
#                 if s in cls.CHARS_CORRECT or s == " ":
#                     return True
#                 else:
#                     raise ValueError("некорректное поле name")
#
#     def __init__(self, name, size=10):
#         if self.check_name(name):
#             self.psw = name
#             self.size = int(size)
#         else:
#             raise ValueError("некорректное поле name")
#
#     def get_html(self):
#         return f"<p class='password'>{self.psw}: <input type='text' size={self.size} />"
#
#
# class FormLogin:
#     def __init__(self, lgn, psw):
#         self.login = lgn
#         self.password = psw
#
#     def render_template(self):
#         return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])
#
#
# # эти строчки не менять
# login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
# html = login.render_template()
# print(html)
#
# PODVIG 8
# from string import ascii_lowercase, digits
#
# class CardCheck:
#     CHARS_FOR_NAME = ascii_lowercase.upper() + digits
#
#     @staticmethod
#     def check_card_number(number):
#         temp_lst = []
#         if number[4] == '-' and number[9] == '-' and number[14] == '-' and (len(number) == 19):
#             temp_str = number.replace('-', '').replace('-', '').replace('-', '')
#             for x in temp_str:
#                 if x in digits:
#                     temp_lst.append(x)
#                 else:
#                     return False
#             return True
#         return False
#
#     @classmethod
#     def check_name(cls, name):
#         temp_lst = []
#         if name.count(' ') == 1:
#             for i, x in enumerate(name):
#                 if x in cls.CHARS_FOR_NAME or x == ' ':
#                     temp_lst.append(x)
#             if len(temp_lst) == len(name):
#                 return True
#             else:
#                 return False
#         return False
#
#
# is_number = CardCheck.check_card_number("1234-5678-9012-0000")
# is_name = CardCheck.check_name("SERGEI BALAKIREV")
# print(is_number, is_name)
#
# PODVIG 9
#
# class Video:
#     def create(self, name):
#         self.name = name
#
#     def play(self):
#         print(f"воспроизведение видео <{self.name}>")
#
#
# class YouTube:
#     videos = []
#     @classmethod
#     def add_video(cls, video):
#         cls.videos.append(video)
#
#
#     @classmethod
#     def play(cls, video_indx):
#         temp = cls.videos[video_indx]
#         Video.play(temp)
#
# v1 = Video()
# v2 = Video()
# v1.create("Python")
# v2.create("Python ООП")
# YouTube.add_video(v1)
# YouTube.add_video(v2)
# YouTube.play(0)
# YouTube.play(1)
#
# PODVIG 10
# class Application:
#     def __init__(self, name, blocked=False):
#         if type(name) == str and type(blocked) == bool:
#             self.name = name
#             self.blocked = blocked
#
#
# class AppStore:
#     appstore_lst = []
#
#     def add_application(self, app):
#         if app not in self.appstore_lst:
#             self.appstore_lst.append(app)
#
#     def remove_application(self, app):
#         for i,x in enumerate(self.appstore_lst):
#             if x == app:
#                 self.appstore_lst.pop(i)
#
#
#     def block_application(self, app):
#         if app in self.appstore_lst:
#             app.blocked = True
#
#     def total_apps(self):
#         return len(self.appstore_lst)
#
#
# store = AppStore()
# app_youtube = Application("Youtube")
#
# store.add_application(app_youtube)
# store.block_application(app_youtube)
# store.remove_application(app_youtube)
#
# # PODVIG 11
# class Message:
#     def __init__(self, str, fl_like=False):
#         self.text = str
#         self.fl_like = fl_like
#
#
# class Viber:
#     lst_message = []
#
#     @classmethod
#     def add_message(cls, msg):
#         cls.lst_message.append(msg)
#
#     @classmethod
#     def remove_message(self, msg):
#         for i, x in enumerate(self.lst_message):
#             if x == msg:
#                 self.lst_message.pop(i)
#     @classmethod
#     def set_like(cls, msg):
#         if msg in cls.lst_message:
#             if msg.fl_like == False:
#                 msg.fl_like = True
#             else:
#                 msg.fl_like = False
#                 print("no")
#     @classmethod
#     def show_last_message(cls):
#         if cls.lst_message != []:
#             return cls.lst_message[-1]
#
#     @classmethod
#     def total_messages(cls):
#         return len(cls.lst_message)
#
#
# msg = Message("Всем привет!")
# Viber.add_message(msg)
# Viber.add_message(Message("Это курс по Python ООП."))
# Viber.add_message(Message("Что вы о нем думаете?"))
# Viber.set_like(msg)
# Viber.remove_message(msg)
