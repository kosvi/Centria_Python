#!/usr/bin/python3

def calculate_combinations(possible_values, length_of_combination):
  if length_of_combination==1:
    return possible_values
  return possible_values*(calculate_combinations(possible_values-1, length_of_combination-1))

print(calculate_combinations(3, 1))
print(calculate_combinations(3, 3))
print(calculate_combinations(3, 2))
print(calculate_combinations(4, 2))
