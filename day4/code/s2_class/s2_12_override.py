class Laptop:
    def __init__(self, 
                width, height, price, color, gpu):
        self.name = 'Vision 학습 작업용 노트북'
        self.w = width
        self.h = height
        self.p = price
        self.c = color
        self.gpu = gpu
        self.available = ['3080', '3090',
                         '4070', '4080', '4090',
                         '5060', '5070', '5080', '5090']


    def printLaptop(self):
        print(self.w, self.h, '노트북 프린트')


    def gpucheck(self):
        if self.gpu in self.available:
            print(f'{self.gpu}: 실습 가능')

        else:
            print(f'{self.gpu}: 실습 불가능')



class Desktop(Laptop):
    def printLaptop(self):
        print(self.w, self.h, '데스크톱 프린트')
    
    def power_on(self):
        print(f'{self}의 전원이 켜짐')


if __name__ == '__main__':
    a = Desktop(40, 30, 200, 'black', '5060')
    a.printLaptop()


    b = Laptop(40, 30, 200, 'white', '5070')
    b.printLaptop()
    