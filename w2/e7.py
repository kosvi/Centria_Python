#!/usr/bin/python3

def count_bills(euros, bill):
  bills = 0
  while euros >= bill:
    bills += 1
    euros -= bill
  printed = False
  if bills>0:
    print(f"{bills}x{bill} euros",end="")
    printed = True
  return euros, printed

euros = int(input("Give the amount of euros: "))

bills = [500, 200, 100, 50, 20, 10, 5]
first = True
for bill in bills: 
  if not first and euros>=bill:
    print(", ",end="")
  euros, printed = count_bills(euros, bill)
  if printed:
    first = False

print("")
print(f"{euros} euros couldn't be converted to bills")
