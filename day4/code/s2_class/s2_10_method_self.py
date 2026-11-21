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


if __name__ == '__main__':
    gpu1 = input('gpu 이름 입력: ')
    a1 = Laptop(40, 30, 200, 'black', gpu1)
    a1.gpucheck()

    gpu2 = input('gpu2 이름 입력: ')
    a2 = Laptop(40, 30, 200, 'white', 4060)
    a2.gpucheck()