#!/usr/bin/python3

rows = 0
while True:
  try:
    char = input("Give char: ")
    if len(char)<1:
      continue
    rows = int(input("# of rows: "))
    if rows<1:
      continue
    break
  except:
    continue

for i in range(rows):
  print(f"{char[0]*(i+1)}")
