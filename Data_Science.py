import numpy as np
# mylist = [1,2,3]
# print(mylist)
# arr = np.array(mylist)
# print(arr)
# print(type(arr))

# my_mat = [[1,2,3],[4,5,6],[7,8,9]]
# print(my_mat)
# arr2 = np.array(my_mat)
# shape_tuple = arr2.shape
# for i in range(shape_tuple[0]):
#     for j in range(shape_tuple[0]):
#         print(f"Row {i+1} element {j+1} = {arr2[i][j]}")

# arr_1 = np.arange(1,21)
# print(arr_1)

#You can reshape the above array of 20 elements by using reshape function
#But the number of factors of 20 will limit the options
# print(arr_1.reshape(4,5))

# zr = np.zeros(3)
# print(zr)

# ls = np.linspace(0,10,5)
# print(ls)

# imat = np.eye(4)
# print(imat)

# arr = np.random.rand(5,5)
# print(arr)

arr = np.random.randint(1,100,20)
arr_2d = arr.reshape(4,5)
# print(arr_2d)
# print(arr_2d.argmax(), arr_2d.max())
#Slicing Array
print(arr_2d)
print(arr_2d[1:3,3:4])