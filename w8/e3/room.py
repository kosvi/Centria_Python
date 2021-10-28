class Room:

  def __init__(self, size=0):
    self.size = size

  @property
  def size(self):
    return self.__size

  @size.setter
  def size(self, size):
    size = max(size, 0)
    size = min(size, 100)
    self.__size = size

  @size.deleter
  def size(self):
    self.__size = 0

  def get_info(self, room):
    return f"{room} is {self.__size} squares"
