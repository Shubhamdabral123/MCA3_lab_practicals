# Write a program to illustrate the indexing and slicing operations in NumPy arrays.

import numpy as np

arr1 = np.array([1, 3, 5, 6, 15, 9, 24, 64, 653, 23])
print("Slicing of the numpy array: ")
print(arr1[4:7])

print("Indexing of the numpy arrays")
print(arr1[2])

# --------------OUTPUT------------------
# Slicing of the numpy array:
# [15  9 24]
# Indexing of the numpy arrays
# 5
