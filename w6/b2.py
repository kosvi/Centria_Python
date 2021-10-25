#!/usr/bin/python3

arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr2 = [2]*10

def multiply_arrays(arr1, arr2):
  arr3 = []
  for a, b, in zip(arr1, arr2):
    arr3.append(a*b)
  return arr3

print("")
print("This function creates a new array without altering those given as parameter.")
print("New array has the length of a shorter array given as parameter. ")

print(f"{arr1}\n{arr2}\n")
print(multiply_arrays(arr1, arr2))
