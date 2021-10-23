#!/usr/bin/python3

length_of_loop = 20

def factorial(n):
  if n<=1:
    return 1
  return n * factorial(n-1)

def approx_cos_recursive(x, n=0, multiplier = 1):
  if n>=length_of_loop:
    return 0
  return multiplier * x**n/factorial(n) + approx_cos_recursive(x, n+2, multiplier*-1)

def approx_cos_loop(x):
  sum = 1
  multiplier = -1
  for n in range(2, length_of_loop, 2):
    sum += multiplier * x**n/factorial(n)
    multiplier *= -1
  return sum

def approx_sin_recursive(x, n=1, multiplier = 1):
  if n>=length_of_loop:
    return 0
  return multiplier * x**n/factorial(n) + approx_sin_recursive(x, n+2, multiplier*-1)

def approx_sin_loop(x):
  sum = x
  multiplier = -1
  for n in range(3, length_of_loop, 2):
    sum += multiplier * x**n/factorial(n)
    multiplier *= -1
  return sum

print(approx_cos_loop(3))
print(approx_cos_recursive(3))

print(approx_sin_loop(3))
print(approx_sin_recursive(3))
