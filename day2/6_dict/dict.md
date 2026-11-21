# 딕셔너리
- {키1:값1, 키2:값2, ...} 형태의 자료구조
- 딕셔너리[키]로 값에 접근 가능
- 반정형 데이터 유형 중 하나인 JSON과 유사
    - JSON과 딕셔너리는 1:1 대응이 가능
- 타 언어에도 같은 개념인 연관배열 또는 해시기 있음

```py
a = {
    1:'a',
    2:'b',
    3:'c'
}

print(a)
```
```
{1: 'a', 2: 'b', 3: 'c'}
```

## 사용 방법
- 딕셔너리[키] -> 해당 키에 대응하는 값 반환
```py
grade = {'pey': 10, 'julliet': 99}
print(grade['pey'])
```
```
10
```

### 쌍 추가, 삭제
```py
# 새로운 키-값 추가
a = {1: 'a'}
a[2] = 'b' # 기존에 없던 새로운 키 2에 값 b를 넣어라
print(a)

# 기존 키-값 삭제
del a[1]
print(a)
```
```
{1: 'a', 2: 'b'}
{2: 'b'}
```

## 주의사항
- 딕셔너리의 Key는 고유한 값이므로 중복되어선 안됨
    - 만약 중복된 키가 있으면 마지막 키만 유지되고, 나머진 무시됨
```py
a = {1:'a', 1:'b'}
print(a)
```
```
{1: 'b'}
```

### 딕셔너리 내부에 딕셔너리 사용 가능
```py
myDict = {
    'name':'abc',
    'age': 25,
    'hobby': {
        'private': '안알려줌',
        'public': ['reading', 'athlate', 'piano']
    }
}

print(myDict)
print(myDict['hobby']['private'])
print(myDict['hobby']['public'][0])
```
```
{'name': 'abc', 'age': 25, 'hobby': {'private': '안알려줌', 'public': ['reading', 'athlate', 'piano']}}
안알려줌
reading
```

## 딕셔너리 함수
### key만 추출
- keys(): 딕셔너리 내 키를 뽑아 리스트(정확히 dict_keys라는 객체)로 반환
    - 진짜 리스트로 바꾸려면 list() 함수 사용
```py
a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print(a.keys())
```
```
dict_keys(['name', 'phone', 'birth'])
```

### value만 추출
- values(): keys()와 마찬가지
```py
a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print(a.values())
```
```
dict_values(['pey', '010-9999-1234', '1118'])
```

### Key-Value 쌍 모두 얻기
- items(): 키-값 쌍 모두 반환
    - [(키, 값)] 형태, 즉 리스트 안에 튜플 형태로 반환

```py
a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print(a.items())
```
```
dict_items([('name', 'pey'), ('phone', '010-9999-1234'), ('birth', '1118')])
```

### 해당 키가 딕셔너리 안에 있는지 조사
- 키 in 딕셔너리 -> True/False 반환
```py
a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}

print('name' in a)
print('email' in a)
```
```
True
False
```

### Key로 Value 꺼내기
- pop(키): 해당 키와 그에 대응하는 값 꺼내서 반환 후 삭제
```py
a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
phone = a.pop('phone')
print(phone)
print(a)
```
```
010-9999-1234
{'name': 'pey', 'birth': '1118'}
```