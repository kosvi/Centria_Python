#!/usr/bin/python3


sum = 0
# let's include 2 and 40
for i in range(2, 42, 2):
  sum += i
print(f"sum of even numbers between 2-40 is {sum}")

sum = 0
i = 2
while i<=40:
  sum += i
  i += 2
print(f"sum of even numbers between 2-40 is {sum}")
