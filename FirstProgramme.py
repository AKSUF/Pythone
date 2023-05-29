# nums=[7,8,9,5]
# it=iter(nums)
# print(it.__next__())
# print(next(it))
# for i in nums:
#     print(i)



# def topten():
#     yield 5
#     yield 10
#     yield 15
#
# values = topten()
#
# print(values.__next__())  # Prints 5
# print(values.__next__())  # Prints 10
#
# for i in values:
#     print(i)  # Prints 15


def topten():
    n=1
    while n<=10:
        sq=n*n
        yield  sq
        n+=1
values=topten()
for i in values:
    print(i)



