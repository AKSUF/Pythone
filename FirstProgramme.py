# from numpy import *
# arr=array([1,2,3,4,5])
# arr=arr+5
# print(arr)

from numpy import *
arr1=array([1,2,3,4,5])
# arr2=array([1,2,3,4,5])

#to create new array
# arr2=arr1.view()
#deep copy
arr2=arr1.copy()
#shallow copy
arr1[1]=7

#vectorized opration
arr3=arr1+arr2
arr2=arr2.view()
print(arr1)
print(arr2)
# concatenated = concatenate((arr1, arr2))
# print(cos(arr3))
# print(sin(arr3))
# print(log(arr3))
# print(sqrt(arr3))
# print(sum(arr3))
# print(min(arr3))
# print(max(arr3))
# print(concatenated)
print(id(arr1))
print(id(arr2))