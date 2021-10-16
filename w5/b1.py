#!/usr/bin/python3

from random import randint

random_array = []
for i in range(20):
  random_array.append(randint(1,100))

print("Array of 20 contains the following: ")
print(random_array)
print("---")
# let's calculate SD

avg = sum(random_array)/len(random_array)
sum_of_squares = 0
for x in random_array:
  sum_of_squares += (x-avg)**2
sd = (sum_of_squares/len(random_array))**(1/2)

print(f"standard deviation: {sd}")
