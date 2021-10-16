#!/usr/bin/python3

def average(arr):
  return sum(arr)/4

def get_values():
  print("insert four values: ")
  arr = []
  for i in range(4) :
    arr.append(float(input("> ")))
  print(f"average of those values is: {average(arr)}")

get_values()
