# Pandas

- Numpy는 인덱스로만 데이터에 접근해야 하지만 Pandas는 열에는 키워드, 행에는 번호나 이름으로 데이터에 접근함

## Series
- 이름표가 붙은 목록
    ```py
    import pandas as pd 
    s = pd.Series([0.91, 0.32, 0.77]) 
    print(s) 
    ```
    ```
    0    0.91
    1    0.32
    2    0.77
    dtype: float64
    ```
- Series 행에 이름 부여 가능
```py
import pandas as pd 
count = pd.Series(
    [12, 5, 3], 
    index=["person", "car", "dog"]
) 

print(count) 
print(count["car"]) # 5 ← 이름표로 찾기 
print(count[count > 4]) # person 12, car 5 ← NumPy 와 같은 조건 고르기 print(count * 2) # 칸마다 계산도 그대로 
print(count.sum()) # 20 
print(count.to_numpy()) # [12 5 3] ← 이름표를 떼면 NumPy 배열
```
```
person    12
car        5
dog        3
dtype: int64
5
person    12
car        5
dtype: int64
20
[12  5  3]
```

- Series끼리 계산
    - 자리 번호가 아닌 이름표를 보고 짝을 맞춤
    - 목록의 순서가 달라도 같은 이름끼리
    - 만약 한 쪽에만 값이 있으면 NaN 반환

```py
import pandas as pd 

mon = pd.Series(
    {"person": 12, "car": 5, "dog": 3}
) 
tue = pd.Series(
    {"car": 7, "person": 10, "bike": 2}
) 

print(mon + tue)
print()
# bike NaN ← 월요일엔 없음 
# car 12.0 ← 5 + 7 
# dog NaN ← 화요일엔 없음 
# person 22.0 ← 12 + 10 

print(mon.add(tue, fill_value=0)) # 짝이 없으면 0 으로 보고 더하기 
```
```
bike       NaN
car       12.0
dog        NaN
person    22.0
dtype: float64

bike       2.0
car       12.0
dog        3.0
person    22.0
dtype: float64
```
## DataFrame
- DataFrame: 시리즈를 여러개 모아놓은 것
#### 만드는 방법
1. 열 단위: "열 이름: 값 목록"
    - `pd.DataFrame(딕셔너리)`
2. 행 단위: 한 줄에 딕셔너리 하나
    - `pd.DataFrame(딕셔너리가 담긴 리스트)`
3. Numpy 배열에 열 이름만 붙이기
    - `pd.DataFrame(넘파이_배열, columns=열_이름이_담긴_리스트)`

```py
import numpy as np 
import pandas as pd 

# 방법 1: 열 단위로 — "열 이름: 값 목록" 
df1 = pd.DataFrame({ 
 "frame": [1, 1, 2, 3, 3], 
 "label": ["person", "car", "person", "dog", "person"], 
 "conf": [0.91, 0.77, 0.85, 0.42, 0.66],
}) 
print('열 단위로 만들기')
print(df1) ;print()


# 방법 2: 줄 단위로 — 한 줄에 딕셔너리 하나 
rows = [] 
rows.append({"frame": 1, "label": "person", "conf": 0.91}) 
rows.append({"frame": 1, "label": "car", "conf": 0.77}) 
df2 = pd.DataFrame(rows) 
print('행 단위로 만들기')
print(df2); print()


# 방법 3: NumPy 배열에 열 이름만 붙이기 
arr = np.random.default_rng(0).random((4, 3)).round(2) 
df3 = pd.DataFrame(arr, columns=["temp", "humid", "dist"]) 
print('NumPy로 만들기')
print(df3) ; print()
```
```
열 단위로 만들기
   frame   label  conf
0      1  person  0.91
1      1     car  0.77
2      2  person  0.85
3      3     dog  0.42
4      3  person  0.66

행 단위로 만들기
   frame   label  conf
0      1  person  0.91
1      1     car  0.77

NumPy로 만들기
   temp  humid  dist
0  0.64   0.27  0.04
1  0.02   0.81  0.91
2  0.61   0.73  0.54
3  0.94   0.82  0.00
```

## 표의 구성 요소
- DataFrame의 열 하나하나가 Series
- 엑셀에서 모든 열이 왼쪽의 행 번호를 함께 쓰는것과 같음
#### 관련 함수/메서드
- `df.shape`: 크기
- `df.columns`: 열 이름 객체 반환
- `df.index`: 행 이름 객체 반환
- `df[열_이름]`: '열_이름'을 가진 데이터프레임의 특정 열을 시리즈로 반환
- `series.to_numpy()`: 시리즈를 넘파이 배열로 변환
    ```py
    import pandas as pd 

    df = pd.DataFrame({ 
    "frame": [1, 1, 2, 3, 3], 
    "label": ["person", "car", "person", "dog", "person"], 
    "conf": [0.91, 0.77, 0.85, 0.42, 0.66], 
    }) 

    print('크기:', df.shape) # (5, 3) ← 5 줄 3 칸 
    print('열 목록:', df.columns.tolist()) # ['frame', 'label', 'conf'] ← 열 이름(머리글) 
    print('행 목록:', df.index.tolist()) # [0, 1, 2, 3, 4] ← 줄 이름표 
    print('열들의 타입\n', df.dtypes) # 열마다 값의 종류 
    print('df[\'conf\']\n', df["conf"],  '\n') # 열 하나 꺼내기 → Series 
    print('df[\'conf\'] (넘파이 변환)\n',df["conf"].to_numpy()) # [0.91 0.77 0.85 0.42 0.66] ← NumPy 배열로

    ```
    ```
    크기: (5, 3)
    열 목록: ['frame', 'label', 'conf']
    행 목록: [0, 1, 2, 3, 4]
    열들의 타입
    frame      int64
    label        str
    conf     float64
    dtype: object
    df['conf']
    0    0.91
    1    0.77
    2    0.85
    3    0.42
    4    0.66
    Name: conf, dtype: float64 

    df['conf'] (넘파이 변환)
    [0.91 0.77 0.85 0.42 0.66]
    ```

## 처음 보는 데이터 점검하기
- `df.head(행_개수)`: 앞에서 행_개수만큼만 표시
    - 매개변수 없으면 앞에서 5개만 출력
- `df.info()`: 데이터프레임의 열마다 열 이름, 개수, 빈 값이 아닌 개수 출력
- `df.describe()`: 숫자 열의 요약 통계 출력
- `df[col_name].value_counts()`: 데이터프레임 내 특정 열(또는 시리즈)의 값 개수 출력

    ```py
    import pandas as pd 

    df = pd.DataFrame({ 
    "camera":\
        ["cam1", "cam1", "cam2", "cam2", "cam1", "cam2"], 
    "label":\
        ["person", "helmet", "car", "Person", "person", "car"],
    "conf": \
        [0.91, 0.85, 0.77, 0.42, None, 0.95], 
    }) 


    print('---head---')
    print(df.head(3)) # 앞 3 줄 보기 (뒤는 tail) 
    print('---info---')
    df.info() # 줄 수, 열별 종류, 빈 값이 아닌 값의 개수 (스스로 출력함) 

    print('---describe---')
    print(df.describe()) # 숫자 열의 개수·평균·최솟값·최댓값 등 요약 

    print('---value_count---')
    print(df["label"].value_counts()) # 값마다 몇 번 나오는지 (많은 순) 

    ```
    ```
    ---head---
    camera   label  conf
    0   cam1  person  0.91
    1   cam1  helmet  0.85
    2   cam2     car  0.77
    ---info---
    <class 'pandas.DataFrame'>
    RangeIndex: 6 entries, 0 to 5
    Data columns (total 3 columns):
    #   Column  Non-Null Count  Dtype  
    ---  ------  --------------  -----  
    0   camera  6 non-null      str    
    1   label   6 non-null      str    
    2   conf    5 non-null      float64
    dtypes: float64(1), str(2)
    memory usage: 276.0 bytes
    ---describe---
            conf
    count  5.000000
    mean   0.780000
    std    0.212368
    min    0.420000
    25%    0.770000
    50%    0.850000
    75%    0.910000
    max    0.950000
    ---value_count---
    label
    person    2
    car       2
    helmet    1
    Person    1
    Name: count, dtype: int64
    ```
#### 위 결과에서...
- info()
    - conf 열에 NaN값 하나 존재
- describe()
    - 수치 데이터가 conf만 있으므로 conf 열에 대한 정보만 출력됨
    - 개수: 5개(아까 결측치 하나 있었음), 평균: 0.78, 표준편차: 0.212, ...
- value_count()
    - label 열에서 'person'은 2개, 'car'은 2개, ...