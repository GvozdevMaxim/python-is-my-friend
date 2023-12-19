class Shop:
    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        if product in self.goods:
            self.goods.remove(product)


class Product:
    count = 1
    attrs_check_collection = {'id': int, 'name': str, 'weight': [int, float], 'price': (int, float)}
    def __init__(self, name, weight, price):
        self.id = Product.count
        Product.count += 1

        self.name = name
        self.weight = weight
        self.price = price

    def __setattr__(self, key, value):
        if key in self.attrs_check_collection and \
                self.attrs_check_collection[key] == type(value) \
                or type(value) in self.attrs_check_collection[key] \
                and key in ('weight', 'price') and value > 0:
            object.__setattr__(self, key, value)
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    def __delattr__(self, item):
        if item == "id":
            raise AttributeError("Атрибут id удалять запрещено.")
        object.__delattr__(self, item)

shop = Shop("Балакирев и К")
book = Product("Python ООП", 100, 1024)
shop.add_product(book)
shop.add_product(Product("Python", 150, 512))
for p in shop.goods:
    print(f"{p.name}, {p.weight}, {p.price}")