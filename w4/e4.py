#!/usr/bin/python3

import random

throws = [0]*6

for i in range(100):
  throws[random.randint(1, 6)-1] += 1

total = 0
for i, value in enumerate(throws):
  print(f"{i+1} was thrown {value} times")
  total += value
print(f"total throws: {total}")
