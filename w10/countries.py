#!/usr/bin/python3

class Countries:

  def __init__(self, filename):
    self.read_from_file(filename)

  def read_from_file(self, filename):
    self.filename = filename
    self.populations = {}
    try: 
      with open(filename) as file_obj:
        for line in file_obj:
          country, population = line.split(",")
          self.populations.update({country.strip(): population.strip()})
    except FileNotFoundError:
      self.status = False
      self.status_text = "FileNotFound"
    except PermissionError:
      self.status = False
      self.status_text = "NoPermission"
    except:
      self.status = False
      self.status_text = "UnknownError"
    else:
      self.status = True
      self.status_text = "OK"

  def print_populations(self):
    if not self.status:
      return
    for key in self.populations.keys():
      print(f"{key}: {self.populations.get(key)}")

  def find_country(self, country):
    if not self.status:
      return
    return self.populations.get(country)

  def add_country(self, country, population):
    if not self.status:
      return False
    if country not in self.populations.keys():
      with open(self.filename, 'a') as file_obj:
        file_obj.write(f"{country},{population}\n")
      self.populations.update({country: population})
      return True
    else:
      return False

  def overwrite_country(self, country, population):
    if not self.status:
      return False
    try:
      with open(self.filename, 'w') as file_obj:
        for key in self.populations.keys():
          file_obj.write(f" {key},{self.populations.get(key)}\n")
      self.populations.update({country: population})
    except PermissionError:
      message = "NoPermission"
      status = False
    except:
      message = "UnknownError"
      status = False
    else:
      message = "OK"
      status = True
    finally:
      return (status, message)

  def find_largest_population(self):
    if not self.status:
      return 
    largest = ("", -1)
    for key in self.populations.keys():
      current = int(self.populations.get(key))
      if largest[1]<current:
        largest = (key, current)
    return largest

