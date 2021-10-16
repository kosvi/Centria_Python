#!/usr/bin/python3

n = int(input("Give n: "))

fac = 1
for i in range(n):
  fac *= (i+1)

print(f"factorial of n is {fac}")
