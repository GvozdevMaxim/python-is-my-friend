class Box:
    def __init__(self):
        self.box_list = list()

    def add_thing(self, obj):
        self.box_list.append(obj)

    def get_things(self):
        return self.box_list

    def __eq__(self, other):
        res1 = sorted(self.box_list, key=lambda x: x.mass)
        res2 = sorted(other.box_list, key=lambda x: x.mass)
        if res1 == res2:
            return True
        else:
            return False



class Thing:
    def __init__(self, name, mass):
        self.name = name
        self.mass = mass

    def __eq__(self, other):
        return self.name.lower() == other.name.lower() and self.mass == other.mass

    def __ne__(self, other):
        return self.name.lower() != other.name.lower() or self.mass != other.mass

    def __lt__(self, other):
        if self.name.lower() < other.name.lower():
            return True
        else:
            return False


b1 = Box()
b2 = Box()

b1.add_thing(Thing('мел', 100))
b1.add_thing(Thing('тряпка', 200))
b1.add_thing(Thing('доска', 2000))

b2.add_thing(Thing('тряпка', 200))
b2.add_thing(Thing('мел', 100))
b2.add_thing(Thing('доска', 2000))

res = b1 == b2  # True
res2 = b1 != b2
print(res)
print(res2)
