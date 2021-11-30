import numpy as np

arr = np.array([[5, 10], [15, 20]])
# Add 10 to element values
print("Adding 10: " + repr(arr + 10))

# Multiple elements by 5
print("Multiplying by 5: " + repr(arr * 5))

# Subtract 5 from elements
print("Subtracting 5: " + repr(arr - 5))

# Matrix multiplication
arr1 = np.array([[-8, 7], [17, 20], [8, -16], [11, 4]])
arr2 = np.array([[5, -5, 10, 20], [-8, 0, 13, 2]])
print("Multiplying two arrays: " + repr(np.matmul(arr1, arr2)))

# Exponential
arr3 = np.array([[1, 5], [2.5, 2]])
# Exponential of each element
print("Taking the exponential: " + repr(np.exp(arr3)))

# Cubing all elements
print("Making each element a power of 3: " + repr(np.power(3, arr3)))
