# while

## 기본 구조
```
while 조건문:
    수행할_문장1
    수행할_문장2
    수행할_문장3
    ...
```
- while 문은 **조건문이 참(*True*)인 동안** while 문에 속한 문장들을 **반복해서** 수행한다.

```py
treeHit = 0

while treeHit < 10:
    treeHit += 1
    print(f'나무를 {treeHit}번 찍었습니다.')

    if treeHit == 10:
        print('나무 넘어갑니다!')
```
```
나무를 1번 찍었습니다.
나무를 2번 찍었습니다.
나무를 3번 찍었습니다.
나무를 4번 찍었습니다.
나무를 5번 찍었습니다.
나무를 6번 찍었습니다.
나무를 7번 찍었습니다.
나무를 8번 찍었습니다.
나무를 9번 찍었습니다.
나무를 10번 찍었습니다.
나무 넘어갑니다!
```

- 만약 조건이 거짓이되는 조건이 없다면 무한루프 발생
    - Ctrl + c 누르면 강제종료
    - 강제 종료가 되면 KeyboardInterrupt 에러 발생
```py
while True:
    print('aaa')
```
```
...(중략)...
aaa
aaa
Traceback (most recent call last):
  File "c:\Users\Admin\Desktop\workspace\python_basic\day3\code\s3_while\s3_2_infinity_loop.py", line 2, in <module>
    print('aaa')
    ~~~~~^^^^^^^
KeyboardInterrupt
```

## input
- input(): 사용자 입력 함수. 입력 시 콘솔에 입력하면 됨
- input()함수가 돌아가는 중에 입력을 계속 안하면 사실상 무한루프

```py
x = input("입력: ")

print(x)
```
```
입력: ㅁㅁㅁ
ㅁㅁㅁ
```

- input()함수는 입력받은 값을 str형으로 반환함
    - 만약 숫자 등 다른 형태의 자료를 입력하려면 형변환 함수를 써줘야 함

```py
# x = input('input: ') # 에러
# input()함수는 입력값을 문자열로 반환함
x= int(input('input:'))

if x >= 100:
    print('1m 이상 객체')
else:
    print('1m 미만 객체')
```
```
input:100
1m 이상 객체
```

### while 예제 하나 만들기
```py
# while문 예제: 목표 금액을 모을 때까지 매달 저축하기

goal = 100000      # 목표 금액
monthly = 15000    # 매달 저축하는 금액
savings = 0        # 현재 모은 금액
month = 0          # 지난 개월 수

# 모은 금액이 목표보다 적은 동안 계속 반복
while savings < goal:
    month += 1
    savings += monthly
    print(f"{month}개월차: {savings}원 저축")

print(f"목표 {goal}원 달성까지 {month}개월이 걸렸습니다!")

```
```
1개월차: 15000원 저축
2개월차: 30000원 저축
3개월차: 45000원 저축
4개월차: 60000원 저축
5개월차: 75000원 저축
6개월차: 90000원 저축
7개월차: 105000원 저축
목표 100000원 달성까지 7개월이 걸렸습니다!
```

## while문 강제로 빠져나가기
- Ctrl + c로 멈출 순 있지만 실제 대부분 소프트웨어는 터미널을 안쓰는 경우가 많음
- 특정 조건에 `break` 키워드 사용

```py
x = 0

while True:
    print('while 실행')
    x += 1 

    if x == 10:
        break
```
```
while 실행
while 실행
while 실행
while 실행
while 실행
while 실행
while 실행
while 실행
while 실행
while 실행
```
<video controls src="20261118-0302-38.3821579.mp4" title="Title"></video>

- 무한루프 탈출 방법
    1. break 키워드 사용
    2. while을 반복하며 while 조건식 조건을 False로 유도

## continue
- continue: 조건문에서 특정 조건에 맞으면 아무것도 실행 안하고 넘어가는 키워드

```py
y = 0


while True:
    y += 1

    if y % 2 == 0:
        print(f'y값: {y:2d}')

    else:
        continue # y가 홀수면 넘어감

    if y == 10:
        break
```

## 무한 루프
- 무한 루프: while문에서 조건이 계속 참이라 무한히 수행되는 상태
- 강제 종료하려면 터미널에서 Ctrl + C 누름

## while-else문
- while 문이 조건이 거짓이 되어 정상적으로 끝나면 else 절이 실행되고, break로 빠져나가면 else 절은 실행되지 않는다.
```py
cnt = 0

while cnt < 3:
    print(f'count: {cnt}')
    cnt += 1

# break로 인한 강제 탈출이 아닌 정상 탈출 경우에 실행
else:
    print('while문이 정상 종료 되었습니다.')
```

## 중첩된 while문
- while문 안에 또 다른 while문 사용 가능

#### 무한루프 내 무한루프
```py
while True:
    print(000)
    while True:
        print(123)
```
```
...
123
123
123
123
123
123
...
```
- while문 조건도 계속 참이지만 while문 내부 조건도 계속 참
    - -> 내부 whlie문 먼저 실행되고 외부 while문은 도달하지 못함

#### 무한루프 내 비 무한루프
```py
while True:
    print('000')
    while True:
        print('123')
        break 
```
-  중첩된 반복문 내 break는 가장 가까운 depth의 반복문 블럭을 찾는다. 그 블럭을 탈출한다.