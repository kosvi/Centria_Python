class Ingredient:

  def __init__(self, name, allergenic):
    self.name = name
    self.allergenic = allergenic

  def to_string(self):
    return self.name
