#!/usr/bin/python3

while True: 
  U = int(input("Give voltage: "))
  I = int(input("Give current: "))
  print(f"\nResistance is {U/I}")
  c = input("Calculate another? (y/n) ")
  if c!='y':
    break
  print("---")
