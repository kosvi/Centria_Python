#!/usr/bin/python3

class Migratory:

  def __init__(self, country, month):
    self.country = country
    self.month = month

  @property
  def country(self):
    return self.__country

  @property
  def month(self):
    return self.__month

  @country.setter
  def country(self, country):
    if len(country)>=5 and len(country)<=20:
      if country[0].isupper():
        self.__country = country
      else:
        raise ValueError("Country name has to start with capital letter", country)
    else:
      raise ValueError("Country length has to be between [5,20]", len(country))

  @month.setter
  def month(self, month):
    if month>=1 and month<=12:
      self.__month = month
    else:
      raise ValueError("Month has to be between [1,12]", month)

  def get_info(self):
    return f"{self.__country}: {self.__month}"

def main():
  while True:
    print("")
    print("type \"quit\" to exit")
    try: 
      c = input("Give name for country: ")
      if c=="quit":
        break
      m = int(input("Give number of month: "))
    except:
      print("incorrect input")
      continue
    try:
      m = Migratory(c, m)
      print(f"\n\t{m.get_info()}")
    except ValueError as e:
      print(e)

if __name__ == "__main__":
  m = Migratory("Empty", 1)
  m.country = "Foobar"
  m.month = 6
  print(m.get_info())
  try:
    m.country = "Foo"
  except ValueError as e:
    print(e)
  try:
    m.month = 13
  except ValueError as e:
    print(e)

  print("\nProgram starts\n")
  main()
