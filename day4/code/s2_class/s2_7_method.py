class Laptop:
    def setData(self, a):
        self.name=a


    def printLaptop(self):
        print(self, '노트북 프린트')



a1 = Laptop()
print(a1)
a1.setData("4070")
a1.printLaptop()
print(a1.name)