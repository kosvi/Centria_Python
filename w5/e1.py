#!/usr/bin/python3

import random

LENGTH_OF_ARRAY = 30

# make array of LENGTH_OF_ARRAY with random values [0,10[
random_array = []
for i in range(LENGTH_OF_ARRAY):
  random_array.append(random.random()*10)

sum = 0.0
for value in random_array:
  sum += value

print(f"sum of array is: {sum}")
print(f"average is: {sum/len(random_array)}")
