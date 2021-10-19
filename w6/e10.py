#!/usr/bin/python3

def search_from_array(arr, value):
  for i, v in enumerate(arr):
    if v==value:
      print(f"found {v} from array with index {i}")

arr = []
print("Add words to array, type 'quit' to exit:")
while(True):
  word = input("> ")
  if word=='quit':
    break
  arr.append(word)

print("Search a word from array:")
search_from_array(arr, input("> "))
