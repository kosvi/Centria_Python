#!/usr/bin/python3

import random

arr1 = []
arr2 = []
for i in range(10):
  arr1.append(random.randint(1,10))
  arr2.append(random.randint(1,10))

print(arr1)
print(arr2)
print("---------------")

# with a oneliner

arr3 = [sum(x) for x in zip(arr1, arr2)]

print(arr3)

# or with a loop

arr4 = []
for i, v in enumerate(arr1):
  arr4.append(arr2[i]+v)

print(arr4)
