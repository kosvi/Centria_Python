#!/usr/bin/python3

days_in_month = [
  31,
  28,
  31,
  30,
  31,
  30,
  31,
  31,
  30,
  31,
  30,
  31
]

month = int(input("Give the month (as integer): "))
if month>0 and month<13:
  month -= 1
  print(f"month has {days_in_month[month]} days")
else:
  print("invalid month")
