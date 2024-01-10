class WordString:

    def __init__(self, strr=""):
        self.__string = strr

    def __len__(self):
        return len(self.__string.split())

    def __call__(self, *args, **kwargs):
        return self.__string.split()[args[0]]

    @property
    def string(self):
        return self.__string

    @string.setter
    def string(self, str):
        self.__string = str


words = WordString()
words.string = "Курс по Python ООП"
n = len(words)
first = "" if n == 0 else words(0)
print(words.string)
print(f"Число слов: {n}; первое слово: {first}")
