class Car:
    # //class variable
    wheels=4

    def __init__(self):
        # instance variable
        self.mil=10
        self.com="BMW"
c1=Car()
c2=Car()
c1.mil=8
# //class variable
Car.wheels=5
print(c1.com,c1.mil,c1.wheels)
print(c2.com,c2.mil,c2.wheels)
