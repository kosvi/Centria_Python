from ingredient import Ingredient

class Recipe:

  def __init__(self, name, cooking_time):
    self.name = name
    self.cooking_time = cooking_time
    self.ingredients = []

  def add_ingredient(self, ingredient):
    self.ingredients.append(ingredient)

  def remove_ingredient(self, ingredient):
    self.ingredients.remove(ingredient)

  def to_string(self):
    string = f"{self.name} ({self.cooking_time})"
    for ig in self.ingredients:
      string += f"\n - {ig.to_string()}"
    return string
