#!/usr/bin/python3

import random

LENGTH_OF_ARRAY = 30

random_array = []
for i in range(LENGTH_OF_ARRAY):
  random_array.append(int(random.random()*10000))

print("Values in array: ", end="")
first = True
for value in random_array:
  if not first:
    print(", ",end="")
  print(f"{value}",end="")
  first = False
print("")

# Find max
max_value = random_array[0]
for value in random_array:
  max_value = max(max_value, value)

print(f"max value is: {max_value}")
