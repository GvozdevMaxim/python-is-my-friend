class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


class Lib:
    def __init__(self):
        self.book_list = []

    def __add__(self, other):
        if type(other) is not Book:
            raise AttributeError("Правый оперант должен быть объектомм класса Book")
        self.book_list.append(other)
        return self

    def __iadd__(self, other):
        if type(other) is not Book:
            raise AttributeError("Правый оперант должен быть объектомм класса Book")
        self.book_list.append(other)
        return self

    def __sub__(self, other):
        if type(other) not in (Book, int):
            raise AttributeError("Правый оперант должен быть объектомм класса Book или int")
        if type(other) is Book:
            self.book_list.remove(other)
            return self
        if type(other) is int:
            self.book_list.pop(other)
            return self

    def __isub__(self, other):
        if type(other) not in (Book, int):
            raise AttributeError("Правый оперант должен быть объектомм класса Book или int")
        if type(other) is Book:
            self.book_list.remove(other)
            return self
        if type(other) is int:
            self.book_list.pop(other)
            return self

    def __len__(self):
        return len(self.book_list)

book = Book("title", "author", 2024)
lib = Lib()

lib = lib + book # добавление новой книги в библиотеку
print(f"Первое сложение {lib.__dict__}")
lib += book
print(f"Второе сложениие {lib.__dict__}")
# lib = lib - book # удаление книги book из библиотеки (удаление происходит по ранее созданному объекту book класса Book)
# print(f"Первое вычитание {lib.__dict__}")
# lib -= book
# print(f"Второе вычитание {lib.__dict__}")
#
lib = lib - 0 # удаление книги по ее порядковому номеру (индексу: отсчет начинается с нуля)
lib -= 0