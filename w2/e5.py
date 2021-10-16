#!/usr/bin/python3

# Euro to dollar
EXC_RATE = 1.16

while True:
  dollars = float(input("Give the amount of dollars\n> ").replace(",","."))
  print(f"{dollars} is {dollars / EXC_RATE} in euros")
  c = input("Make another conversion (y/n) ")
  if c!='y':
    break;
  print("---")
