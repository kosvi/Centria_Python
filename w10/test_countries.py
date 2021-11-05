import os
from countries import Countries

def test_find_country():
  # https://stackoverflow.com/questions/5137497/find-the-current-directory-and-files-directory
  dirpath = os.path.dirname(os.path.realpath(__file__))
  c = Countries(f"{dirpath}/countries.txt")
  assert c.find_country("Finland") == "5508198"

