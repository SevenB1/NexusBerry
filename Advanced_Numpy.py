import numpy as np
# # import matplotlib as mt
# A = np.arange(6).reshape(3,2)
# B = np.arange(6).reshape(2,3)
# print(A)
# print(B)
# print(A @ B) Multiply

ar1 = np.random.randint(1,20,10).reshape(2,5)
ar2 = np.random.randint(1,20,10).reshape(2,5)
print(np.unique(np.isin(ar1, ar2)))
print(ar1)
print(ar2)
ar1[1:] = ar2[:1] #Exchanging columns

print(ar1)