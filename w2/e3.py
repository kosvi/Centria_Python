#!/usr/bin/python3

def printAns(v, s):
  while True: 
    selection = input("a) in hours\nb) in whole hours and minutes\n> ")
    if selection=='a':
      print(f"Time driven is {s/v} hours")
      return
    if selection=='b':
      minutes = int(60*s/v - 60*(int(s/v)))
      print(f"Time driven is {int(s/v)} h {minutes} min")
      return

while True:
  v = int(input("Give speed of the car.\n> "))
  s = int(input("Give distance driven.\n> "))
  printAns(v, s)
  c = input("Calculate another? (y/n) ")
  if c!='y':
    break
  print("---")
