#!/usr/bin/python3

import random

row = []
i = 0
while i<7:
  num = random.randint(1, 40)
  if not num in row:
    row.append(num)
    i+=1

row.sort()

print(row)
