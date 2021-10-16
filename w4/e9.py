#!/usr/bin/python3

base = float(input("Give base: "))
exp = int(input("Give exponent: "))

value = 1
for i in range(exp):
  value *= base

print(f"{base}^{exp} = {value}")
