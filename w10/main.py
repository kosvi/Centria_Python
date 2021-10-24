#!/usr/bin/python3 

import countries as C
import shutil

def main():
  c = C.Countries("countries.txt")
  # c.overwrite_country("Tuvalu", "1000000")
  c.print_populations()
  largest = c.find_largest_population()
  print(largest)
  print(f"Finland: {c.find_country('Finland')}")

if __name__ == "__main__":
  # let's start with unmodified file
  shutil.copy2("countries.txt.orig", "countries.txt")
  main()
