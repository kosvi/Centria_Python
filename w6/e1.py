#!/usr/bin/python3

def average(a, b):
  return (a+b)/2

def get_average():
  a = int(input("Give first value: "))
  b = int(input("Give second value: "))
  print(f"Average is {average(a, b)}")

get_average()
