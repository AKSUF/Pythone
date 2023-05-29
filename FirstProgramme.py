class PyChamp:
    def execute(self):
        print("Compiling")
        print("Running")
class MyEditor:
    def execute(self):
        print("spell Check")
        print("Convenstion check")

class Laptop:
    def code(self,ide):
        ide.execute()

ide=PyChamp()
lap1=Laptop()
lap1.code(ide)
