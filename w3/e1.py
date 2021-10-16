#!/usr/bin/python3

while True:
  value = 0
  try: 
    value = int(input("Give a value (0=exit)\n> "))
  except:
    print("You have to give a numerical value")
    continue
  if value>100:
    print("Value was > 100")
  elif value==0:
    print("Goodbye!")
    break
  else:
    print("Value was <= 100")
