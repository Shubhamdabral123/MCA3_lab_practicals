# Write a program to add two matrices using function.

import numpy as np


def addmatrix(matrix1, matrix2):
    matrix = np.add(matrix1, matrix2)
    print("Sum of the two matrix: ")
    print()
    print(matrix)


arr1 = np.array([[12, 15, 123],
                 [10, 1, 85]])
arr2 = np.array([[34, 31, 51],
                 [1, 3, 4]])
addmatrix(arr1, arr2)

# ----------OUTPUT---------#

# Sum of the two matrix:

# [[ 46  46 174]
# [ 11   4  89]]

# -------------------------#
