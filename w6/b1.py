#!/usr/bin/python3

def selection_sort(arr):
  for a in range(len(arr)):
    smallest = arr[a]
    index = a
    for b in range(len(arr)-a):
      if arr[b+a]<smallest:
        smallest = arr[b+a]
        index = b+a
    if index!=a:
      tmp = arr[a]
      arr[a] = smallest
      arr[index] = tmp

arr = [3, 4, 6, 1, -2, 8, 4]
arr2 = [-1, 0, -1]
arr3 = [9, 8]
arr4 = [0]
arr5 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6]
print(arr)
selection_sort(arr)
print(arr)
print(arr2)
selection_sort(arr2)
print(arr2)
print(arr3)
selection_sort(arr3)
print(arr3)
print(arr4)
selection_sort(arr4)
print(arr4)
print(arr5)
selection_sort(arr5)
print(arr5)
