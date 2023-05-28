from numpy import *
# def update(x):
#     print(id(x))
#     x = 8
#     print(x)
#     print(id(x))
#     return x
#
# a = 10
# update(a)
# print(a)
# print(id(a))


from numpy import *
def update(lst):
    print(id(lst))
    lst[1]=25
    print(lst)
    print(id(lst))
    return lst

lst=[10,20,30]
print(lst)
update(lst)
print(lst)
print(id(lst))


