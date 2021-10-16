#!/usr/bin/python3

def bmi(w, h):
  return w/(h/100)**2

weight = int(input("weight in kg: "))
height = int(input("height in cm: "))

print(f"bmi: {bmi(weight, height)}")
