from recipe import Recipe

class Cookbook:

  def __init__(self, name, owner):
    self.name = name
    self.owner = owner
    self.recipes = []

  def add_recipe(self, recipe):
    self.recipes.append(recipe)

  def remove_recipe(self, recipe):
    self.recipes.remove(recipe)

  def to_string(self):
    string = f"{self.name} is a cookbook owned by {self.owner}"
    string += f"\nIt contains following recipes: "
    for r in self.recipes:
      string += f"\n{r.to_string()}"
    return string
