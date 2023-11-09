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
    for j in range(shape_tuple[1]):
        print(f"Row {i+1} element {j+1} = {arr2[i][j]}")