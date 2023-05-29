
# def is_even(n):
#     return n%2==0
# name=[3,2,6,4,2,9]
# events=list(filter(is_even,name))
# print(events)


name=[3,2,6,4,2,9]
events=list(filter(lambda n:n%2==0,name))
print(events)