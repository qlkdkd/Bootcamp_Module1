class Calc:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result


calc1 = Calc()
calc2 = Calc()

print(calc1.add(3))
print(calc1.add(4))

print(calc2.add(3))
print(calc2.add(7))