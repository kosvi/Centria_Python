#!/usr/bin/python3

# https://stackoverflow.com/questions/4555932/public-or-private-attribute-in-python-what-is-the-best-way

class Bird:

  __eggs = 0
  _name = ""

  @property
  def eggs(self):
    return self.__eggs

  @eggs.setter
  def eggs(self, value):
    if value>0 and value<11:
      self.__eggs = value

  @eggs.deleter
  def eggs(self):
    self.__eggs = 0

  @property
  def name(self):
    return self._name

  @name.setter
  def name(self, value):
    self._name = value

  @name.deleter
  def name(self):
    self._name = ""

  def get_info(self):
    return f"{self._name} is a bird that has {self.__eggs} eggs"

bird = Bird()
print(bird.eggs)
bird.eggs = 5
print(bird.eggs)
bird.eggs = 12
print(bird.eggs)

print(bird.get_info())
bird.name = "Bob"
print(bird.get_info())
bird.eggs = 0
print(bird.get_info())
bird.name = "May"
print(bird.get_info())
bird.eggs = 8
print(bird.get_info())
del bird.name
print(bird.get_info())
bird._name = "Jack"
del bird.eggs
print(bird.get_info())
bird.eggs = 4
print(bird.get_info())
bird.eggs = 100
bird.__eggs = 100
print(bird.get_info())
print(f"{bird.eggs} vs. {bird.__eggs}")
