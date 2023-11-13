# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
import matplotlib.pyplot as plt
import random

# mylist = [1, 2, 3]
# arr = np.array(mylist)
# print(arr)
# print(type(arr))
#
# my_mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(my_mat)
# mat = np.array(my_mat)
# print(mat)
#
# arr_1 = np.arange(0, 10)
# print(arr_1)
# arr_2 = np.arange(0, 11, 2)
# print(arr_2)
#
# zr = np.zeros(3)
# print(zr)
# zr_2d = np.zeros((5, 5))
# print(zr_2d)
#
# onz = np.ones((3, 4))
# print(onz)
#
# ls = np.linspace(0, 5, 10)
# print(ls)
# ls1 = np.linspace(0, 5, 100)
# print(ls1)
#
# imat = np.eye(4)
# print(imat)
#
# arr = np.random.rand(5)
# print("np.random.rand(5)",arr)
# arr_2d = np.random.rand(5, 5)
# print("np.random.rand(5,5)",arr_2d)
#
# arrn = np.random.randn(2)
# print("np.random.randn(2)",arrn)
# arrn_2d = np.random.randn(4, 4)
# print("np.random.randn(4,4)",arrn_2d)

# arr_int = np.random.randint(1, 100)
# print(arr_int)
arr_ints = np.random.randint(1, 100, 10)
print(arr_ints)

# arr = np.arange(25)
# print(arr)
# arr_2d = arr.reshape(5, 5)
# print(arr_2d)
#
print(arr_ints.max())
print(arr_ints.min())
#
# print(arr_ints)
print(arr_ints.argmax())
print(arr_ints.argmin())
#
# print(arr_2d.shape)
# arr = np.arange(0, 11)
print(arr_ints)
print(arr_ints[8])
print(arr_ints[1:5])
print(arr_ints[:5])
print(arr_ints[5:])
#
arr_ints[:5] = 100
print(arr_ints)
slice_of_arr = arr_ints[:6]
# slice_of_arr[:] = 99
# print(arr)
#
arr_copy = arr_ints.copy()
# arr_copy[0:5] = 100
# print(arr_copy)
# print(arr)
#
arr_2d = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])
print(arr_2d)
#
print(arr_2d[0])
print(arr_2d[1])
print(arr_2d[2])
#
print(arr_2d[0, 0])
print(arr_2d[1, 2])
print(arr_2d[2, 2])
#
print(arr_2d[:2])
print(arr_2d[:2, 1:])
#

print("Start of Boolean indexing in numpy array")
arr = np.arange(1, 11)
print(arr)
print(arr > 5)
bool_arr = arr > 5
print(bool_arr)
#
print("arr[arr > 5]\n",arr[arr > 5])
print("arr[arr > 5]\n",arr[arr < 3])

print("arr[arr >= 5 and arr <= 9]\n",arr[(arr >= 5) & (arr <= 9)])

#Class Exercise:
#Generate a numpy array of 20 elements and reshape with 4x5 dimension and return elements >=11 and <=18
#
array=np.random.randint(1,20,20)
arrayshape=array.reshape(4,5)
print(arrayshape[(arrayshape>11) & (arrayshape<18)])


# arr_1d = np.arange(50)
# print(arr_1d)
# arr_2d = np.arange(50).reshape(5, 10)
# print(arr_2d)
# print(arr_2d[1:3])
# print(arr_2d[1:3, 3:5])
#
arr1 = np.random.randint(1,50,20)
arr2 = np.random.randint(1,50,20)
print(arr1)
print(arr2)
arr1 = arr1.reshape(4,5)
arr2 = arr2.reshape(4,5)
print(arr1)
print(arr2)

# arr3 = arr1 + arr2
# print(arr3)
# arr3 = arr1 - arr2
# print(arr3)
# #
# arr3 = arr1 * arr2
# print(arr3)
#
# arr2 = arr + 100
# print(arr2)
#
# arr2 = arr * 100
# print(arr2)
#
print(arr2)
arr3 = arr2 ** 2
print(arr3)
#
arr4 = np.sqrt(arr3)
print(arr4)
#
# print(np.max(arr2))
# print(np.sin(arr2))
# # print(np.log(arr2))
#
# # Exercise Solutions
# # Create an array of 10 zeros
# print(np.zeros(10))
# # Create an array of 10 ones
# print(np.ones(10))
# # Create an array of 10 5s
# print(np.ones(10) * 5)
# print(np.zeros(10) + 5)
# print(np.full((10), 5))
#
# # create 10 to 50 integer array
# print(np.arange(10, 51))
# # create 10 to 50 even integer array
# print(np.arange(10, 51, 2))
# # create 3x3 matrix values ranging from 0 to 8
# print(np.arange(9))
# print(np.arange(9).reshape(3, 3))
# # Create 3x3 identity matrix
# print(np.eye(3))
# # find the a random number between 0 and 1
# print(np.random.rand(1))
#
x = np.array([1, 0, 2, 3])
print("Original array:")
print(x)
print("Test if none of the elements of the said array is zero:")
print(np.all(x))
#
x = np.array([1, 0, 0, 0])
print("Original array:")
print(x)
print("Test whether any of the elements of a given array is non-zero:")
print(np.any(x))
x = np.array([0, 0, 0, 0])
print("Original array:")
print(x)
print("Test whether any of the elements of a given array is non-zero:")
print(np.any(x))
#
a = np.array([1, 0, np.nan, np.inf])
print("Original array")
print(a)
print("Test a given array element-wise for finiteness :")
print(np.isfinite(a))
#
a = np.array([1, 0, np.nan, np.inf])
print("Original array")
print(a)
print("Test element-wise for NaN:")
print(np.isnan(a))
#
a = np.array([1 + 1j, 1 + 0j, 4.5, 3, 2, 2j])
print("Original array")
print(a)
print("Checking for complex number:")
print(np.iscomplex(a))
print("Checking for real number:")
print(np.isreal(a))
print("Checking for scalar type:")
# print(np.isscalar(3.1))
# print(np.isscalar([3.1]))
#
# x = np.array([3, 5])
# y = np.array([2, 5])
# print("Original numbers:")
# print(x)
# print(y)
# print("Comparison - greater")
# print(np.greater(x, y))
# print("Comparison - greater_equal")
# print(np.greater_equal(x, y))
# print("Comparison - less")
# print(np.less(x, y))
# print("Comparison - less_equal")
# print(np.less_equal(x, y))
#
X = np.array([1, 7, 13, 105])
print("Original array:")
print(X)
print("Size of the memory occupied by the said array:")
print("%d bytes" % (X.size * X.itemsize))
#
# array = np.arange(30, 71)
# print("Array of the integers from 30 to70")
# print(array)
#
# v = np.arange(15, 55)
# print("Original vector:")
# print(v)
# print("All values except the first and last of the said vector:")
# print(v[1:-1])
#

x = np.arange(21)
print("Original vector:")
print(x)
print("After changing the sign of the numbers in the range from 9 to 15:")
x[(x >= 9) & (x <= 15)] *= -1
print(x)

x = np.random.randint(0, 11, 5)
print("Vector of length 5 filled with arbitrary integers from 0 to 10:")
print(x)
#
# m = np.arange(10, 22).reshape((3, 4))
# print(m)
#
# m = np.arange(10, 22).reshape((3, 4))
# print("Original matrix:")
# print(m)
# print("Number of rows and columns of the said matrix:")
# print(m.shape)
#

x = np.ones((5,5))
print(x)
#one on borders
x = np.ones((10, 10))
x[1:-1, 1:-1] = 0
print(x)
#
# x = np.diag([1, 2, 3, 4, 5])
# print(x)
#
#0 and 1 are staggered
x = np.zeros((4, 4))
x[::2, 1::2] = 1
x[1::2, ::2] = 1
print(x)
#
# x = np.array([[0, 1], [2, 3]])
# print("Original array:")
# print(x)
# print("Sum of all elements:")
# print(np.sum(x))
# print("Sum of each column:")
# print(np.sum(x, axis=0))
# print("Sum of each row:")
# print(np.sum(x, axis=1))
#
# x = np.arange(12).reshape(4, 3)
# print("Original array:")
# print(x)
# header = 'col1 col2 col3'
# np.savetxt('temp.txt', x, fmt="%d", header=header)
# print("After loading, content of the text file:")
# result = np.loadtxt('temp.txt')
# print(result)
#
#
#
# # Compute the x and y coordinates for points on a sine curve
# x = np.arange(0, 3 * np.pi, 0.2)
# y = np.sin(x)
# print("Plot the points using matplotlib:")
# plt.plot(x, y)
# plt.show()
