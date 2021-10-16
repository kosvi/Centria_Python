#!/usr/bin/python3

import random

random_array = []
for i in range(10):
  random_array.append(random.randint(1,10))

print(f"our array: {random_array}")
search_value = int(input("search a value: "))

results = {}
for i, value in enumerate(random_array):
  if value==search_value: 
    results[i] = value

if len(results)>0:
  print(f"found {len(results)} matches!")
  print("value was found from indexes: ",end="")
  first = True
  for k in results.keys():
    if not first:
      print(", ",end="")
    print(k,end="")
    first = False
  print("")
else:
  print("no matches found!")
