# Write a program to demonstrate the usage of different element wise array functions.

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 56, 7, 8, 9, 17, 12])
print("Original array: ")
print(arr)

# Adding new element in the array using append function
arr2 = np.append(arr, [43, 543, 654, 232, 895])
print("Array after appending new element: ")
print(arr2)

# Calculating the sum of the array:
sumofarray = np.sum(arr2)
print("Sum of a new array: ")
print(sumofarray)

# Calculating the length of a new array;
length = np.shape(arr2)
print("Length of a array: ")
print(length)

# Calculating the mean of a array:
print("Mean of the array")
mean = np.mean(arr2)
print(mean)

# Calculating the median of a array:
print("Median of the array: ")
median = np.median(arr2)
print(median)

# finding the max of the array:
print("Max of the array: ")
maximum = np.max(arr2)
print(maximum)

# finding the min of the array:
print("Min of the array: ")
minimum = np.min(arr2)
print(minimum)

# -----------OUTPUT--------------------------

# Original array:
# [ 1  2  3  4  5 56  7  8  9 17 12]
# Array after appending new element:
# [  1   2   3   4   5  56   7   8   9  17  12  43 543 654 232 895]
# Sum of a new array:
# 2491
# Length of a array:
# (16,)
# Mean of the array
# 155.6875
# Median of the array:
# 10.5
# Max of the array:
# 895
# Min of the array:
# 1
