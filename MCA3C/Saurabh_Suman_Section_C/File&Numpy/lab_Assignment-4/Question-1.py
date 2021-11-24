# Write a program to perform basic arithmetic operations in a NumPy array.

import numpy as np

arr1 = np.array([7, 4, 1, 5, 2, 9, 8, 12])
arr2 = np.array([1, 4, 5, 6, 7, 8, 9, 10])

print("Sum of the data of arr1 using numpy: ")
sumofarray = np.sum(arr1)
print(sumofarray)

print("Sum of two array using numpy: ")
addition = np.add(arr1, arr2)
print(addition)

print("subtraction of the two array: ")
subtraction = np.subtract(arr1, arr2)
print(subtraction)

print("Multiplication of the two array: ")
multiplication = np.multiply(arr1, arr2)
print(multiplication)

print("Division of the two matrix: ")
division = np.divide(arr1, arr2)
print(division)

# ----------------- OUTPUT -------------------

# Sum of the data of arr1 using numpy:
# 48
# Sum of two array using numpy:
# [ 8  8  6 11  9 17 17 22]
# subtraction of the two array:
# [ 6  0 -4 -1 -5  1 -1  2]
# Multiplication of the two array:
# [  7  16   5  30  14  72  72 120]
# Division of the two matrix:
# [7.         1.         0.2        0.83333333 0.28571429 1.125
# 0.88888889 1.2       ]
