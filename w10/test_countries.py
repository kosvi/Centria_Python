from countries import Countries

def test_find_country():
  c = Countries("countries.txt")
  assert c.find_country("Finland") == "5508198"

