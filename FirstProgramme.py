from functools import reduce

def add_all(a,b):
    return a*b
name=[3,2,6,4,2,9]
events=list(filter(lambda n:n%2==0,name))
doubles=list(map(lambda n:n*2,events))
print(doubles)
sum=reduce(lambda a,b:a+b,doubles)
print(sum)