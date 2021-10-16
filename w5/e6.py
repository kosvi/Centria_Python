#!/usr/bin/python3

from random import randint

def brackets():
  print("check if there is a closing bracker for all brackers")
  some_string = input("give calculation with brackets in it: ")
  stack = []
  for char in some_string:
    if char=='(':
      stack.append('(')
    elif char==')':
       try:
         stack.pop()
       except:
         print("there was a closing bracket without opening bracket")
         stack.append('error')
         break
  
  if len(stack)<1:
    print("all brackets was closed correctly")
  else:
    print("all brackets were not closed correctly")

def count_x():
  random_array = []
  for i in range(10):
    random_array.append(randint(0,9))
  print(random_array)
  num = int(input("Give a number from range [0,9]\n> "))
  print(f"{num} appeared {random_array.count(num)} times in the array")

def sorter():
  my_array = []
  print("Give numbers (0 to finish")
  while True:
    num = int(input("> "))
    if num==0:
      break
    my_array.append(num)
# This is a shallow copy. 
# Should the array contain objects, 
# only a reference to them is copied and it
# will still point to the original object
  original_array = my_array.copy()
  my_array.sort()
  print("Your numbers from smallest to biggest: ")
  for value in my_array:
    print(f"{value} ",end="")
  print("")
  print("Your numbers from biggest to smallest: ")
  my_array.reverse()
  for value in my_array:
    print(f"{value} ",end="")
  print("")
  print("Your original input was: ")
  for value in original_array:
    print(f"{value} ",end="")
  print("")

while True:
  print("---")
  print("a) brackets")
  print("b) count x")
  print("c) sort numbers")
  print("x) anything else to exit")
  s = input("> ")
  if s=='a':
    brackets()
  elif s=='b':
    count_x()
  elif s=='c':
    sorter()
  else:
    break

