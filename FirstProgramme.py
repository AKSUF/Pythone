
from abc import ABC,abstractmethod
class Computer(ABC):
    @abstractmethod
    def process(self):
     pass
class Laptop(Computer):
  def process(self):
      print("it's running")
class Programmer:
    def work(self,com):
        print("Solving Bugs")
class Whiteboard(Computer):
    def process(self):
        print("it's running")
# com=Computer()
com1=Laptop()
com2=Whiteboard()

# com.process()
com1.process()
