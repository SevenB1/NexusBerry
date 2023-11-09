import numpy as np

mylist = [1,2,3]
print(mylist)
arr = np.array(mylist)
print(arr)
print(type(arr))

my_mat = [[1,2,3],[4,5,6],[7,8,9]]
print(my_mat)
arr2 = np.array(my_mat)
shape_tuple = arr2.shape
for i in range(shape_tuple[0]):
    for j in range(shape_tuple[0]):
        print(f"Row {i+1} element {j+1} = {arr2[i][j]}")

arr_1 = np.arange(1,21)
print(arr_1)

#You can reshape the above array of 20 elements by using reshape function
#But the number of factors of 20 will limit the options
print(arr_1.reshape(4,5))

zr = np.zeros(3)
print(zr)