#!/usr/bin/python3

def biggest_from_five(a, b, c, d, e):
  return biggest_from_array([a,b,c,d,e])

def biggest_from_array(arr):
  b = arr[0]
  for v in arr:
    if v>b: 
      b=v
  return b

print(biggest_from_five(1,2,3,4,5))
print(biggest_from_five(5,4,3,2,1))
print(biggest_from_five(-1,-2,-3,-4,-5))
print(biggest_from_five(1,-2,3,-4,-5))
