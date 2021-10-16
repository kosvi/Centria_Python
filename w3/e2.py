#!/usr/bin/python3

weekdays = [
  "monday",
  "tuesday",
  "wednesday",
  "thursday",
  "friday",
  "saturday",
  "sunday"
]

num = int(input("Give number of the day: "))
if num > 0 and num < 8:
  num = num - 1
  print(f"day is {weekdays[num]}")
