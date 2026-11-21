class Laptop:
    def setdata(self, 
                width, height, price, color):
        #self.name = 'Vision 학습 작업용 노트북'
        self.w = width
        self.h = height
        self.p = price
        self.c = color


    def printLaptop(self):
        print(self.w, self.h, '노트북 프린트')



a1 = Laptop()
a1.setdata(40, 30, 200, 'Black')
print(a1.w, a1.h, a1.p, a1.c)


# 클래스명으로 접근해서 메서드 사용
a3 = Laptop()
Laptop.setdata(a3, 40, 30, 150, 'black')
a3.printLaptop()