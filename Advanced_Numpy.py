import numpy as np
# # import matplotlib as mt
# A = np.arange(6).reshape(3,2)
# B = np.arange(6).reshape(2,3)
# print(A)
# print(B)
# print(A @ B)

ar1 = np.random.randint(1,20,10).reshape(2,5)
ar2 = np.random.randint(1,20,10).reshape(2,5)
# print(np.isin(ar1, ar2))
# print(np.unique(ar1[ar1 != ar2]))
print(ar1)
print(ar2)
ar1[1:0] = ar2[0:0]

print(ar1)