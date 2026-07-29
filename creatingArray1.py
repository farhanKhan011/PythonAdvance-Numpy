# ----------------Creating Arrays in Numpy----------------------
'''
Create a NumPy ndarray Object
NumPy is used to work with arrays. The array object in NumPy is called ndarray.

We can create a NumPy ndarray object by using the array() function.
'''
# Example 
# import numpy as np

# myarr = np.array([1,2,3,4,5])

# print(myarr)
# print(type(myarr))

'''
To create an ndarray, we can pass a list, tuple or any array-like object into the array() method, and it will be converted into an ndarray:

Example
Use a tuple to create a NumPy array:

'''
# import numpy as np 

# arr = np.array((1,2,3,4))

# print(arr)
# print(type(arr))

'''
Dimensions in Arrays
A dimension in arrays is one level of array depth (nested arrays).

nested array: are arrays that have arrays as their elements.

'''
'''
0-D Arrays
0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array.
'''
# Exaple : Create a 0-D array with value 42 | zero 0 dimensional array

# import numpy as np

# myarr = np.array([72])
# myarr = np.array('m')
# print(myarr)

# print('it is ',np.ndim(myarr),'dimensional array ')

'''
1-D Arrays
An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.

These are the most common and basic arrays.

Example
Create a 1-D array containing the values 1,2,3,4,5:

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)

'''

'''
2-D Arrays
An array that has 1-D arrays as its elements is called a 2-D array.

These are often used to represent matrix or 2nd order tensors.

NumPy has a whole sub module dedicated towards matrix operations called numpy.mat

Example
Create a 2-D array containing two arrays with the values 1,2,3 and 4,5,6:
'''

# import numpy as np

# arr = np.array([[1, 2, 3], [4, 5, 6]])

# print(arr)

'''
3-D arrays
An array that has 2-D arrays (matrices) as its elements is called 3-D array.

These are often used to represent a 3rd order tensor.

Example
Create a 3-D array with two 2-D arrays, both containing two arrays with the values 1,2,3 and 4,5,6:

'''
# import numpy as np

# my3dArr = np.array([
#     [[1,2,5,7],[3,4,6,8]],
#     [[1,2,5,7],[3,4,6,8]]
#     ])

# print(np.ndim(my3dArr))

'''
Check Number of Dimensions?
NumPy Arrays provides the ndim attribute that returns an integer that tells us how many dimensions the array have.

Example
Check how many dimensions the arrays have:

import numpy as np

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)
'''

'''

Higher Dimensional Arrays
An array can have any number of dimensions.

When the array is created, you can define the number of dimensions by using the ndmin argument.

Example
Create an array with 5 dimensions and verify that it has 5 dimensions:
'''

# import numpy as np 

# my5dArr = np.array([1,2,3,4,5], ndmin=5)

# print(my5dArr)
# print("The array is ", np.ndim(my5dArr) ,'dimensional array')

