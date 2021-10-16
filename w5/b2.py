#!/usr/bin/python3

math_grades = [5, 5, 6, 7, 7, 8, 9, 9, 10, 10]
eng_grades  = [6, 7, 6, 5, 7, 9, 8, 9, 9, 10]

def calculate_avg(arr):
  return sum(arr)/len(arr)

def calculate_sd(arr):
  avg = calculate_avg(arr)
  sum_of_squares = 0
  for x in arr:
    sum_of_squares += (x-avg)**2
  return (sum_of_squares/len(arr))**(1/2)

def calculate_correlation(arr1, arr2):
  avg_arr1 = calculate_avg(arr1)
  avg_arr2 = calculate_avg(arr2)
  sum_of_products = 0
  for x, y in zip(arr1, arr2):
    sum_of_products += (x-avg_arr1)*(y-avg_arr2)
  return sum_of_products/(calculate_sd(arr1)*calculate_sd(arr2))*(1/len(arr1))

print(calculate_correlation(math_grades, eng_grades))

print(calculate_correlation([4, 5, 6],[4, 5, 6]))
print(calculate_correlation([10, 8, 4],[4, 4, 10]))
