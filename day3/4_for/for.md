# for문

```py
for 변수 in 리스트(또는 튜플, 문자열):
    수행할_문장1
    수행할_문장2
```

### 기본 예시
```py
for i in [1, 2, 3, 4]:
    print(i)
```
```
1
2
3
4
```
- `[1, 2, 3, 4]` 리스트의 첫 번째 요소인 1이 먼저 i 변수에 대입된 후 print(i)문장 수행
- 다음 두번째 요소 2가 i변수에 대해 print(i) 수행
- 마지막 요소까지 반환

#### for문의 대상
- 리스트, 튜플 등 순서를 가진 여러 자료를 담은 자료형

## for문 응용
### 특정 요소 개수
```py
cnt = 0

find_char = input('찾을 문자 입력: ')


for i in "hello":
    if i == find_char:
        cnt += 1

print(f'찾는 문자 {find_char}: {cnt}개')
```
```
찾을 문자 입력: h
찾는 문자 h: 1개
```

- 원본 문자열과 특정 문자를 직접 입력하기
```py
cnt = 0

target = input('원본 문자열')
find = input('찾는 문자')

for i in target:
    if  i == find:
        cnt += 1

print(f'{target}에서 {find} 개수: {cnt}개')
```
```
원본 문자열akdvn;ankwlfdqwfpwqn
찾는 문자c
akdvn;ankwlfdqwfpwqn에서 c 개수: 0개
```

### for과 while의 결합
```py
while True:
    cnt = 0
    target = input('원본 문자열: ')
    find = input('찾을 문자: ')

    for i in target:
        if i == find:
            cnt += 1

    if cnt == 0:
        print('찾는 문자가 없음')
        break

    else:
        print('찾은 문자 개수:', cnt)
        break
print('while 밖')
```
```
원본 문자열: asdf
찾을 문자: a
찾은 문자 개수: 1
while 밖
```
```
원본 문자열: asdf
찾을 문자: c
찾는 문자가 없음
while 밖
```

## for과 while의 차이
- while은 조건을 기반으로, for은 요소의 길이로 반복
    - \~\~\~ 될 때까지: while
    - \~를 소비할 때까지: for

## for문과 continue
- for문 내 if문과 같이 사용 가능
```py
# marks2.py
marks = [90, 25, 67, 45, 80]

number = 0 
for mark in marks: 
    number = number + 1 
    if mark < 60:
        continue 
    print(f"{number}번 학생 축하합니다. 합격입니다.")
```
```
1번 학생 축하합니다. 합격입니다.
3번 학생 축하합니다. 합격입니다.
5번 학생 축하합니다. 합격입니다.
```

## for문 중첩
- for문 내 for문을 쓸 때 외부 for변수와 내부 for 변수의 이름은 달라야 함
- 만약 둘이 같으면 내부 for문이 외부 for문 변수를 같이 써버림
```py
for i in '12345':
    for j in 'asdfg':
        print(i, j, end='  ')
    print()
```
```
1 a  1 s  1 d  1 f  1 g  
2 a  2 s  2 d  2 f  2 g  
3 a  3 s  3 d  3 f  3 g  
4 a  4 s  4 d  4 f  4 g  
5 a  5 s  5 d  5 f  5 g 
```

## range
- 요소가 여러개: 반복 가능한 객체
    - 리스트, 튜플, 문자열 등

- 보통 for문을 돌리려 임의의 리스트를 따로 만드는 경우는 없음
- 만약 이런 객체가 없으면 range() 사용

```py
class range(
 start: SupportsIndex,
 stop: SupportsIndex,
 step: SupportsIndex = 1,
 /
)
```
```
range(stop) -> range object
range(start, stop[, step]) -> range object

Return an object that produces a sequence of integers from start (inclusive)
to stop (exclusive) by step. range(i, j) produces i, i+1, i+2, ..., j-1.
start defaults to 0, and stop is omitted! range(4) produces 0, 1, 2, 3.
These are exactly the valid indices for a list of 4 elements.
When step is given, it specifies the increment (or decrement).
```
- range()는 범위를 만드는 객체
```py
# 리스트 예시
print(range(10))

print(range(0, 10)) # range(10)과 동일

print(list(range(10)))
```
```
range(0, 10)
range(0, 10)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### range()와 for문
```py
for i in range(5): # 0부터 4까지
    print('aaaaaa')
```
```
aaaaaa
aaaaaa
aaaaaa
aaaaaa
aaaaaa
```

### range() 구성
- range(시작 인덱스, 끝 인덱스, 범위)
    - 시작 인덱스의 기본값: 0
    - 범위의 기본값: 1
        - 범위를 다른 정수로 하면 해당 범위만큼 반복
        - 범위를 -1로 지정하면 역순
```py
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(0, len(a), 2):
    print(a[i])
```
```
1
3
5
7
9
```

## list comprehension
- 리스트 안에 for문을 포함하는 방법
- 목적: 리스트 요소를 채우기
```py
a = [1, 2, 3, 4]
result = [num*3 for num in a]
print(result)
```
[3, 6, 9, 12]

- range 활용 가능

```py
a = [i * 10 for i in range(10)]
print(a)
```
```
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
```

### 리스트 컴프리헨션에 조건 추가
```py
[표현식 for 항목 in 반복_가능_객체 if 조건문]
```

```py
a = [1, 2, 3, 4]

result = [num*3 for num in a if num % 2==0]
print(result)
```
```
[6, 12]
```

### 항목 여러개 사용
```py
result1 = [x * y  for x in range(1, 10) for y in range(1, 5)]
print(result1)

# 얘랑 같음
result2 = []
for x in range(1, 10):
    for y in range(1, 5):
        result2.append(x * y)

print(result2)

print(result1 == result2)
```
```
[1, 2, 3, 4, 2, 4, 6, 8, 3, 6, 9, 12, 4, 8, 12, 16, 5, 10, 15, 20, 6, 12, 18, 24, 7, 14, 21, 28, 8, 16, 24, 32, 9, 18, 27, 36]
[1, 2, 3, 4, 2, 4, 6, 8, 3, 6, 9, 12, 4, 8, 12, 16, 5, 10, 15, 20, 6, 12, 18, 24, 7, 14, 21, 28, 8, 16, 24, 32, 9, 18, 27, 36]
True
```

## for - else
```py
for i in range(5):
    print(i, end=' ')

else:
    print('\nfor문 정상 종료')
```
```
0 1 2 3 4 
for문 정상 종료
```

## enumerate
```py
class enumerate(
 iterable: Iterable[str],
 start: int = 0
)
```
```
Return an enumerate object.

iterable
 an object supporting iteration

The enumerate object yields pairs containing a count (from start, which
defaults to zero) and a value yielded by the iterable argument.

enumerate is useful for obtaining an indexed list:
 (0, seq[0]), (1, seq[1]), (2, seq[2]), ...
 ```


```py
fruits = ['apple', 'banana', 'orange']
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
```

- enumerate는 인덱스와 값을 반환
```py
fruits = ['apple', 'banana', 'orange']
print(tuple(enumerate(fruits)))
```
```
((0, 'apple'), (1, 'banana'), (2, 'orange'))
```

- enumerate는 enumerate 객체
```py
fruits = ['apple', 'banana', 'orange']
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
    print(type(i), type(fruit))

print(type(enumerate(fruits)))
```
```
0: apple
<class 'int'> <class 'str'>
1: banana
<class 'int'> <class 'str'>
2: orange
<class 'int'> <class 'str'>
<class 'enumerate'>
```

## zip
- 2개 이상의 리스트 순회할 때 사용
```py
for 항목1, 항목2, 항목3, ... in zip(리스트1, 리스트2, 리스트3, ...):
    ...
```

```py
names = ['홍길동', '김철수', '이영희']
scores = [85, 92, 78]
for name, score in zip(names, scores):
    print(f"{name}: {score}점")
```
```
홍길동: 85점
김철수: 92점
이영희: 78점
```