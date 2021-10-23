#!/usr/bin/python3

def neper(k):
  if k==0:
    return 1
  return 1/factorial(k) + neper(k-1)

def factorial(n):
  if n<=1:
    return 1
  return n * factorial(n-1)

print(neper(k=10))
