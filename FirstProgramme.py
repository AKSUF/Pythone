class A:
    def __init__(self):
        print("in A init")

    def features1(self):
        print("Features 1A working")

    def features2(self):
        print("Features 2B working")


class B(A):
    def __init__(self):
        super().__init__()
        print("in B init")

    def feature3(self):
        print("Feature 3B working")

    def feature4(self):
        print("Feature 4B working")


class C(B, A):
    def __init__(self):
        super().__init__()  # Call B's __init__ method
        A.__init__(self)  # Call A's __init__ method
        print("in C init")
    def feat(self):
        super().features2()


c1 = C()
c1.features1()
c1.feat()

