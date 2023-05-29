class A:
    def features1(self):
        print("Features 1 working")
    def features2(self):
        print("Features 2 working")
class B(A):
    def feature3(self):
        print("Feature 3 working")
    def feature4(self):
        print("Feature 4 working")
class C(B):
    def features5(self):
        print("Features 5 is working")

    def features6(self):
        print("Features 6 is working")

class D:
    def features7(self):
        print("Features 7 working")
    def features8(self):
        print("Features 8 working")

class E(A,D):
    def features9(self):
        print("Features 9 working")

    def features10(self):
        print("Features 10 working")
a1=A()
a1.features1()
a1.features2()
b1=B()
b1.features1()
b1.features2()
c1=C()
c1.features1()
e1=E()
e1.features1()
