# -------------Ufunc Products--------------

'''
Products:
To find the product of the elements in an array, use the prod() function.
'''
# Find the product of the elements of this array:
# import numpy as np
# arr = np.array([1, 2, 3, 4])
# x = np.prod(arr)
# print(x)
# ans is 24 because 1 x 2 x 3 x 4 = 24

# Find the product of the elements of two arrays:
# import numpy as np
# arr1 = np.array([1, 2, 3, 4])
# arr2 = np.array([5, 6, 7, 8])
# x = np.prod([arr1,arr2])
# print(x)
# it Returns 40320 because it multiplies all the elements of both arrays togather from first element to last of element

'''
Product Over an Axis
If you specify axis=1, NumPy will return the product of each array.
'''
# Perform summation in the following array over 1st axis:
# import numpy as np
# arr1 = np.array([1,2,3])
# arr2 = np.array([4,5,6])
# x = np.prod([arr1,arr2], axis = 1 )
# print(x)

'''
Cummulative Product:
Cummulative product means taking the product partially.
E.g. The partial product of [1, 2, 3, 4] is [1, 1*2, 1*2*3, 1*2*3*4] = [1, 2, 6, 24]
Perfom partial sum with the cumprod() function.
'''
# Take cummulative product of all elements for following array:
# import numpy as np 
# arr = np.array([1,2,3,4])
# newarr = np.cumprod(arr)
# print(newarr)
# Returns:[ 1  2  6 24]

# ------------Numpy Ufunc Products Completed-------------
