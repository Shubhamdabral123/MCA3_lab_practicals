# Write a program to sort a numPy array using a function.
import numpy as nm
from numpy.core.fromnumeric import sort


def sorting(array):
    return sort(array)


arr = nm.array([3, 2, 0, 1, 6, 5, 9, 7, 8])
print("Original array: ")
print(arr)
sorted_Array = sorting(arr)
print("Sorted array: ")
print(sorted_Array)

# --------OUTPUT--------#
# Original array:
# [3 2 0 1 6 5 9 7 8]
# Sorted array:
# [0 1 2 3 5 6 7 8 9]
# ----------------------#
