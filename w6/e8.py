#!/usr/bin/python3

def calculate_factorial(n):
  if n==1:
    return 1
  return n*calculate_factorial(n-1)

def calculate_combinations(n, k):
  if n==k:
    return 1
  if n<k:
    return 0
  return calculate_factorial(n)/(calculate_factorial(k)*calculate_factorial(n-k))

print(calculate_combinations(40, 7))
print(calculate_combinations(3, 3))
print(calculate_combinations(4, 5))
