#!/usr/bin/python3

weight = float(input("Give weight: ").replace(",","."))
height = float(input("Give height: ").replace(",","."))

bmi = weight/(height/100)**2

print(f"BMI is {bmi}")

if bmi<18.5:
  print("you are underweight")
elif bmi<24.9:
  print("you are normal weight")
elif bmi<29.9:
  print("you are overweight")
else:
  print("you are obese")
