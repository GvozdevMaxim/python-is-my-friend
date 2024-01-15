class Budget:
    def __init__(self):
        self.budget_list = []


    def add_item(self, it):
        self.budget_list.append(it)

    def remove_item(self, indx):
        if self.budget_list[indx] in self.budget_list:
            self.budget_list.pop(indx)

    def get_items(self):
        return self.budget_list


class Item:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def __add__(self, other):
        all_money = self.money + other.money
        return all_money

    def __radd__(self, other):
        all_money2 = self.money + other
        return all_money2

my_budget = Budget()
my_budget.add_item(Item("Курс по Python ООП", 2000))
my_budget.add_item(Item("Курс по Django", 5000.01))
my_budget.add_item(Item("Курс по NumPy", 0))
my_budget.add_item(Item("Курс по C++", 1500.10))

# вычисление общих расходов
s = 0
for x in my_budget.get_items():
    s = s + x
