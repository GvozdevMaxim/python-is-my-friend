class Body:
    def __init__(self, name, ro, volume):
        if type(name) is str and (type(volume) and type(ro) in (int, float)):
            self.name = name
            self.ro = ro
            self.volume = volume
        else:
            self.name = self.ro = self.volume = None

    def __eq__(self, other):
        if type(other) == Body:
            return self.ro * self.volume == other.ro * other.volume
        else:
            return self.ro * self.volume == other

    def __lt__(self, other):
        if type(other) == Body:
            return self.ro * self.volume < other.ro * other.volume
        else:
            return self.ro * self.volume < other

maxim = Body("Maxim", 940, 0.06)
irochka = Body("Iro4ka", 940, 0.05)
print(maxim == irochka)
print(irochka < 10)
print(maxim > irochka)