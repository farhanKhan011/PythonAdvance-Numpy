# ----------------Simple Arithmetic  Ufunc--------------

'''
Simple Arithmetic
You could use arithmetic operators + - * / directly between NumPy arrays, but this section discusses an extension of the same where we have functions that can take any array-like objects e.g. lists, tuples etc. and perform arithmetic conditionally.
Arithmetic Conditionally: means that we can define conditions where the arithmetic operation should happen.
All of the discussed arithmetic functions take a where parameter in which we can specify that condition.
'''
# ***********************Addition******************
'''
The add() function sums the content of two arrays, and return the results in a new array.
'''
# Add the values in arr1 to the values in arr2:
# import numpy as np 
# arr1 = np.array([1,2,3,4,5])
# arr2 = np.array([2,4,8,16,32])
# newarr = np.add(arr1,arr2)
# print(newarr)
# the above example adds the corresponding elements of both array


# ***********************Subtraction******************
'''
The subtract() function subtracts the values from one array with the values from another array, and return the results in a new array.
'''
# Subtract the values in arr2 from the values in arr1:
# import numpy as np 
# arr1 = np.array([20,40,60,80])
# arr2 = np.array([10,30,50,70])
# newArr = np.subtract(arr1, arr2)
# print(newArr) 
# the result from this example = [10 10 10 10] as it comes from 20-10 , 40-30 , 60 - 50 , 80 - 70 


# ***********************Multiplication******************
'''
The multiply() function multiplies the values from one array with the values from another array, and return the results in a new array.
'''
# Multiply the values in arr1 with the values in arr2:
# import numpy as np 
# arr1 = np.array([2,3,4,5,6])
# arr2 = np.array([1,5,6,8,9])
# newarr = np.multiply(arr1,arr2)
# print(newarr)

# ***********************Division******************
'''
The divide() function divides the values from one array with the values from another array, and return the results in a new array.
'''
# Divide the values in arr1 with the values in arr2:
# import numpy as np 
# arr1 = np.array([40,32,68,90,64])
# arr2 = np.array([5,16,68,2,10])
# newarr = np.divide(arr1,arr2)
# print(newarr)

# ***********************Power******************
'''
The power() function rises the values from the first array to the power of the values of the second array, and return the results in a new array.
'''
# Raise the valules in arr1 to the power of values in arr2:
# import numpy as np 
# arr1 = np.array([2,3,4,5])
# arr2 = np.array([2,2,2,2])
# newarr = np.power(arr1,arr2)
# print(newarr)

# ***********************Power******************
'''
Both the mod() and the remainder() functions return the remainder of the values in the first array corresponding to the values in the second array, and return the results in a new array.
'''
# Return the remainders:
# import numpy as np 
# arr1 = np.array([10,21,26,37])
# arr2 = np.array([3,2,5,9])
# newarr = np.mod(arr1 , arr2)
# print(newarr)

# You get the same result when using the remainder() function:

# Return the remainders:
# import numpy as np 
# arr1 = np.array([10,21,26,37])
# arr2 = np.array([3,2,5,9])
# newarr = np.remainder(arr1 , arr2)
# print(newarr)

# ***********************Quotient and Mod******************
'''
The divmod() function return both the quotient and the mod. The return value is two arrays, the first array contains the quotient and second array contains the mod.
'''
# Return the quotient and mod:
# import numpy as np 
# arr1 = np.array([10,21,26,37])
# arr2 = np.array([3,2,5,9])
# newarr = np.divmod(arr1 , arr2)
# print(newarr)
# The output has two arrays : The first array represents the quotients,The second array represents the remainders of the same divisions.

# ***********************Absolute Values******************
'''
Both the absolute() and the abs() functions do the same absolute operation element-wise but we should use absolute() to avoid confusion with python's inbuilt math.abs()
'''
# Return the absolute values of the array:
# import numpy as np
# arr = np.array([-1, -2, 1, 2, 3, -4])
# newarr = np.absolute(arr)
# print(newarr)

# The example above will return [1 2 1 2 3 4].Positive values 

# -----------------Ufunc Arithmetic Completed---------------------



