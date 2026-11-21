# 내장 함수
- 다루지 않았던것들 위주로...

## filter
- filter(함수명, 반복가능한_데이터): 반복 가능한 데이터 중 함수에 만족하는 것만 리스트로 반환
    ```py
    def positive(x):
        return x > 0


    print(
        list(filter(
            positive, [1, -3, 2, 0, -5, 6]
        ))
    )
    ```
    ```
    [1, 2, 6]
    ```

- 보통 함수를 사용할 때는 뒤에 괄호를 함께 붙여주지만, 결국 함수명도 변수임
    - 즉 일부 함수에서는 함수명을 인수로 사용할 수 있음
- 함수명은 함수를 지칭하는 변수(포인터)

#### + ai생성 코드의 문제점
```py
class laptop:
    pass


a = laptop
a()
```
- 이처럼 문법이 통일되지 않는다고 함
- 우리는 이런걸 구분하기 위해 적어도 문법을 알아야 함


## isinstance
- isinstance(objcet, class): 객체가 해당 클래스의 인스턴스인지 판단하는 함수

```py
class A:
    pass

a = A()
b = 1

print(isinstance(a, A))
print(isinstance(b, A))
```
```
True
False
```

## map
- map(function, iterable): 함수 f와 반복 가능한 데이터를 입력으로 받음
```py
a, b =map(int, input().split())
print(a, b)
```
```
1 2
1 2
```