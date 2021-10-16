#!/usr/bin/python3

import math

triangles_by_sides = [
  "equilateral",
  "isosceles",
  "scalene"
]
triangles_by_angles = [
  "right",
  "acute",
  "oblique"
]

def calculate_side(a, b, c):
  if a==b and b==c:
    return 0
  if a==b or b==c:
    return 1
  return 2

def calculate_angle(a, b, c):
  sides = [a, b, c]
  sides.sort()
  h = math.sqrt(sides[0]**2 + sides[1]**2)
  if h==sides[2]:
    return 0
  if sides[2]>h:
    return 2
  return 1

print("Give lengths of triangles sides: ")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
by_sides = triangles_by_sides[calculate_side(a, b, c)]
by_angles = triangles_by_angles[calculate_angle(a, b, c)]
print(f"triangle is {by_sides} {by_angles} angled triangle")
