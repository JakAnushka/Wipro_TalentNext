'''1. Create two dimensional 3*3 array and perform ndim, shape, slicing operation on it.'''
import numpy as np

arr2d = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

print("Dimensions:", arr2d.ndim)

print("Shape:", arr2d.shape)

print("First row:", arr2d[0])              
print("Second column:", arr2d[:, 1])       
print("Element at (2,3):", arr2d[1, 2])    
print("Sub-matrix:\n", arr2d[0:2, 1:3]) 

'''2. Create one dimensional array and perform ndim, shape, reshape operation on it'''

arr1d = np.array([10, 20, 30, 40, 50, 60])


print("Dimensions:", arr1d.ndim)

print("Shape:", arr1d.shape)

reshaped_arr = arr1d.reshape(2, 3)
print("Reshaped to 2x3:\n", reshaped_arr)
