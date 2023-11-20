import numpy as np
# # import matplotlib as mt
# A = np.arange(6).reshape(3,2)
# B = np.arange(6).reshape(2,3)
# print(A)
# print(B)
# print(A @ B) Multiply

# ar1 = np.random.randint(1,20,10).reshape(2,5)
# ar2 = np.random.randint(1,20,10).reshape(2,5)
# print(np.unique(np.isin(ar1, ar2)))
# print(ar1)
# print(ar2)
# ar1[1:] = ar2[:1] #Exchanging columns

# print(ar1)

# import numpy as np

# # Create two sample arrays
# array1 = np.array([[1, 2, 3],
#                    [4, 5, 6],
#                    [7, 8, 9]])

# array2 = np.array([[11, 12, 13],
#                    [14, 15, 16],
#                    [17, 18, 19]])

# # Choose the columns to exchange
# column_to_exchange1 = 1
# column_to_exchange2 = 2

# # Swap the columns
# array1[:, [column_to_exchange1, column_to_exchange2]] = array1[:, [column_to_exchange2, column_to_exchange1]]
# array2[:, [column_to_exchange1, column_to_exchange2]] = array2[:, [column_to_exchange2, column_to_exchange1]]

# print("Array 1 after column exchange:\n", array1)
# print("\nArray 2 after column exchange:\n", array2)