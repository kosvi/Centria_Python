#!/usr/bin/python3

def sum_of_array(arr):
  # would be eary with using sum(arr)
  sum = 0
  for value in arr:
    sum += value
  return sum

arr = [1, 2, 3]
print(f"sum of the array is {sum_of_array(arr)}")
