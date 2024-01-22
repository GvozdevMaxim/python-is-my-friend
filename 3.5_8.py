class MoneyR:
    def __init__(self, volume=0):
        self.__volume = volume
        self.__cb = None

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, value):
        self.__cb = value

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, value):
        self.__volume = value

    def __eq__(self, other):
        return abs(self.cb - other.cb) < 0.1

    def __gt__(self, other):
        return self.cb > other.cb

    def __ge__(self, other):
        return self.cb >= other.cb

class MoneyD:
    def __init__(self, volume=0):
        self.__volume = volume
        self.__cb = None

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, value):
        self.__cb = value

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, value):
        self.__volume = value

    def __eq__(self, other):
        return abs(self.cb - other.cb) < 0.1

    def __gt__(self, other):
        return self.cb > other.cb

    def __ge__(self, other):
        return self.cb >= other.cb

class MoneyE:
    def __init__(self, volume=0):
        self.__volume = volume
        self.__cb = None

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, value):
        self.cb = value

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, value):
        self.__volume = value

    def __eq__(self, other):
        return abs(self.cb - other.cb) < 0.1

    def __gt__(self, other):
        return self.cb > other.cb

    def __ge__(self, other):
        return self.cb >= other.cb
class CentralBank:

    rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def register(cls, money):
        money.__cb = cls


CentralBank.rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

r = MoneyR(45000)
d = MoneyD(500)

CentralBank.register(r)
CentralBank.register(d)

if r > d:
    print("неплохо")
else:
    print("нужно поднажать")