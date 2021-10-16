#!/usr/bin/python3

weight = float(input("Give your weight (kg)\n> "))
height = float(input("Give your height (cm)\n> "))

print(f"You BMI is {weight/(height/100)**2}")
