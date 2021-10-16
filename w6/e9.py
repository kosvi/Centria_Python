#!/usr/bin/python3

# let's calculate SD

def calculate_sd(arr): 
  avg = sum(arr)/len(arr)
  sum_of_squares = 0
  for x in arr:
    sum_of_squares += (x-avg)**2
  sd = (sum_of_squares/len(arr))**(1/2)
  return sd

print("separate numbers with comma and space: \", \"")
values = input("Insert values: ")
# https://stackoverflow.com/questions/7368789/convert-all-strings-in-a-list-to-int
arr = list(map(int, values.split(", ")))
print(f"standard deviaton: {calculate_sd(arr)}")
