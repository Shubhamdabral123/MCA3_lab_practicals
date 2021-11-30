import numpy as np
 
# Create a sequence of integers from 10 to 1 with a step of -2
a = np.arange(10, 1, -2)
print("\n A sequential array with a negative step: \n",a)



# Arrange elements from 0 to 19
b = np.arange(20)
print("\n Array is:\n ",b)
 
# b[start:stop:step]
print("\n b[-8:17:1] = ",b[-8:17:1])
 
# The : operator means all elements till the end.
print("\n b[10:] = ",b[10:])
