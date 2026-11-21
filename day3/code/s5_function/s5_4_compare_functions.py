# 리턴값이 있는 함수
def add1(a, b):
    return a + b


# 리턴값이 없는 함수
def add2(a, b):
    print(f'sum of {a} + {b} is {a+b}')


print(add1(10, 20))
print(add2(10, 20)) # 함수가 호출이 되지만 반환값은 없음

ret1 = add1(10, 20)
ret2 = add2(10, 20)

print(ret1, ret2)