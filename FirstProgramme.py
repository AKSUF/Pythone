# def person(name,age):
#     print(name)
#     print(age-5)
# # person('navin',67)
# person(age=28,name="navin")

#
# def person(name,age=18):
#     print(name)
#     print(age)
# # person('navin',67)
# person("navin",28)


#//////////////////////
import numpy as np
def sum(a, *b):
    c = np.sum((a, *b))
    print(c)

sum(5, 6, 8, 9)
