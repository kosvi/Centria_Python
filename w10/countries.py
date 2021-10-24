#!/usr/bin/python3

class Countries:

  def __init__(self, filename):
    self.filename = filename
    self.populations = {}
    with open(filename) as file_obj:
      for line in file_obj:
        country, population = line.split(",")
        self.populations.update({country.strip(): population.strip()})

  def print_populations(self):
    for key in self.populations.keys():
      print(f"{key}: {self.populations.get(key)}")

  def find_country(self, country):
    return self.populations.get(country)

  def add_country(self, country, population):
    if country not in self.populations.keys():
      self.populations.update({country: population})
      with open(self.filename, 'a') as file_obj:
        file_obj.write(f"{country},{population}\n")
      return True
    else:
      return False

  def overwrite_country(self, country, population):
    self.populations.update({country: population})
    with open(self.filename, 'w') as file_obj:
      for key in self.populations.keys():
        file_obj.write(f" {key},{self.populations.get(key)}\n")

  def find_largest_population(self):
    largest = ("", -1)
    for key in self.populations.keys():
      current = int(self.populations.get(key))
      if largest[1]<current:
        largest = (key, current)
    return largest

