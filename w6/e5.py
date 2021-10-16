#!/usr/bin/python3

def biggest(a, b, c):
  return max(a, max(b, c))

print(biggest(1,2,3))
print(biggest(-1,-2,-3))
print(biggest(9,-4,7))
