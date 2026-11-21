from s2_10_method_self import Laptop

class Desktop(Laptop):
    def power_on(self):
        print(f'{self}의 전원이 켜짐')


if __name__ == '__main__':
    a = Desktop(40, 30, 200, 'black', '5060')
    a.power_on()