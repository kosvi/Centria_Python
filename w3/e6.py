#!/usr/bin/python3

def way1(a, b, c):
  values = [a, b, c]
  values.sort()
  return values[2]

def way2(a, b, c):
  return max(a, max(b, c))

def way3(a, b, c):
  biggest = a
  if b>biggest:
    biggest = b
  if c>biggest:
    biggest = c
  return biggest

print("Give three values: ")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

print("Biggest value is: ")
print(way1(a, b, c))
print(way2(a, b, c))
print(way3(a, b, c))
