# #This program is to illustrate access modifiers of a class
# class super:
#     #public data member
#     var1 = None

#     #protected data member
#     _var2 = None

#     #private data member
#     __var3 = None

#     #constructor
#     def __init__(self,var1,var2,var3):
#         self.var1 = var1
#         self._var2 = var2
#         self.__var3 = var3

#     #public member function
#     def displayPublicMembers(self):
#         #accessing public data members
#         print("Public Data member:",self.var1)

#     # protected member function
#     def _displayProtectedMembers(self):
#             # accessing protected data members
#             print("Protected Data member:", self._var2)

#     # private member function
#     def __displayPrivateMembers(self):
#         # accessing private data members
#         print("Private Data member:", self.__var3)

#     #public member function
#     def accessPrivateMembers(self):
#         self.__displayPrivateMembers()


# #derive class
# class Sub(super):
#     #constructor
#     def __init__(self,var1,var2,var3):
#         super.__init__(self,var1,var2,var3)
#     #public member function
#     def accessProtectedMembers(self):
#         #accessing protected member functions of super class
#         self._displayProtectedMembers()

# #creating objects of the derived class
# obj = Sub("Nexusberry",4,"DSML")

# #calling public member functions of the class
# obj.displayPublicMembers()
# obj.accessProtectedMembers()
# obj.accessPrivateMembers()

# print(obj.var1)

# superobj = super("Nexusberry",4,"DSML")
# # print(superobj.__var3)
# superobj.accessPrivateMembers()
# print(obj._var2)

