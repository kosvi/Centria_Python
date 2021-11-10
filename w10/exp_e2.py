#!/usr/bin/python3

def convert_to_year(year):
  try:
    year = int(year)
  except ValueError as e:
    raise ValueError("Year has to be given as numerical value", year)
    return year
  if year<0:
    raise ValueError("Year can not be below zero", year)
  if year>3000:
    raise ValueError("Year has to be below 3001", year)
  return year

def main():
  while True:
    try:
      year = convert_to_year(input("Give year (0 to quit): "))
      if year==0:
        break
      print(year)
    except Exception as e:
      print(e)

if __name__ == "__main__":
  main()
