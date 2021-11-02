#!/usr/bin/python3


def factorial(n):
  if n<0:
    return -1
  if n<=1:
    return 1
  else:
    return n*factorial(n-1)


if __name__ == "__main__":
  print(factorial(-1))
  print(factorial(0))
  print(factorial(2))
  print(factorial(10))
