#!/usr/bin/python3


sum = 0
for i in range(5, 101, 5):
  sum += i
print(f"sum of numbers 5, 10, ... 100 is {sum}")

sum = 0
i = 5
while i<=100:
  sum += i
  i += 5
print(f"sum of numbers 5, 10, ... 100 is {sum}")
