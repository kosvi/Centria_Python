#!/usr/bin/python3 

from cookbook import Cookbook
from recipe import Recipe
from ingredient import Ingredient as ig

def main():
  print("")
  cb = Cookbook("My recipes", "Ville")
  r = Recipe("Meatballs", "15 min")
  meat = ig("Meat", False)
  balls = ig("Balls", False)
  r.add_ingredient(meat)
  r.add_ingredient(balls)
  cb.add_recipe(r)
  print(cb.to_string())
  print("\n----\n")
  zucchini = ig("Zucchini", True)
  r2 = Recipe("Zucchini balls", "45 min")
  r2.add_ingredient(zucchini)
  r2.add_ingredient(balls)
  cb.add_recipe(r2)
  print(cb.to_string())

if __name__ == "__main__":
  main()
