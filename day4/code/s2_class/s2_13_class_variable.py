class Laptop:

    # 클래스 변수
    available = [
        '3080', '3090',
        '4070', '4080', '4090',
        '5060', '5070', '5080', '5090']

    
    def __init__(self, 
                width, height, price, color, gpu):

        # 인스턴스 변수
        self.name = 'Vision 학습 작업용 노트북'
        self.w = width
        self.h = height
        self.p = price
        self.c = color
        self.gpu = gpu


    def printLaptop(self):
        print(self.w, self.h, '노트북 프린트')


    def gpucheck(self):
        if self.gpu in self.available:
            print(f'{self.gpu}: 실습 가능')

        else:
            print(f'{self.gpu}: 실습 불가능')


a = Laptop(10, 20, 30, 'red', '5060')
print(a.available)
a.gpucheck()

b = Laptop(20, 30, 40, 'blue', '4060')
a.available.append('4060')

print(b.available)
b.gpucheck()