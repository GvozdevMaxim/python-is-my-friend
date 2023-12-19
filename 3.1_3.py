class Book:
    def __init__(self, title='', author='', pages=0, year=0):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

    def __setattr__(self, key, value):
        if key == "title" and type(value) is not str:
            raise TypeError("Неверный тип присваиваемых данных.")
        elif key == "author" and type(value) is not str:
            raise TypeError("Неверный тип присваиваемых данных.")
        elif key == "pages" and type(value) is not int:
            raise TypeError("Неверный тип присваиваемых данных.")
        elif key == "year" and type(value) is not int:
            raise TypeError("Неверный тип присваиваемых данных.")
        else:
            object.__setattr__(self, key, value)


book = Book("Python ООП", "Сергей Балакирев", 123, 2022)
