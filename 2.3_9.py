class Recipe:
    def __init__(self, *args):
        self.arguments = list(args)

    def add_ingredient(self, ing):
        self.arguments.append(ing)

    def remove_ingredient(self, ing):
        if ing in self.arguments:
            self.arguments.remove(ing)

    def get_ingredients(self):
        return tuple(self.arguments)

    def __len__(self):
        return len(self.arguments)


class Ingredient:
    def __init__(self, name, volume, measure):
        self.name = name
        self.volume = volume
        self.measure = measure

    def __str__(self):
        return f"{self.name}: {self.volume}, {self.measure}"

recipe = Recipe()
recipe.add_ingredient(Ingredient("Соль", 1, "столовая ложка"))
recipe.add_ingredient(Ingredient("Мука", 1, "кг"))
recipe.add_ingredient(Ingredient("Мясо баранины", 10, "кг"))
ings = recipe.get_ingredients()
n = len(recipe) # n = 3
print(n)