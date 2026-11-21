class Laptop:
    def __init__(self, 
                width, height, price, color):
        self.name = 'Vision 학습 작업용 노트북'
        self.w = width
        self.h = height
        self.p = price
        self.c = color


    def printLaptop(self):
        print(self.w, self.h, '노트북 프린트')



a1 = Laptop(40, 30, 200, 'Black')
print(a1.name, a1.w, a1.h, a1.p, a1.c)