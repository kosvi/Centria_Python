#!/usr/bin/python3

# https://math.stackexchange.com/questions/2916718/calculating-the-square-root-of-2/2916723

def sqrt_of_x(x, d):
  i=0
  y = 1
  while i<d:
    y = calculate_decimal(y, x)
    i+=1
  return round(y, d)

def calculate_decimal(y, x):
  return 0.5*(y+(x/y))

print("Square root of 2:")
print(sqrt_of_x(2, 1))
print(sqrt_of_x(2, 3))
print(sqrt_of_x(2, 5))
print(sqrt_of_x(2, 10))
print("Square root of 13:")
print(sqrt_of_x(13, 4))
print(sqrt_of_x(13, 6))

