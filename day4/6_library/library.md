# 라이브러리
- 파이썬 언어로만 모든 걸 구현하기는 한계가 있음
- 이때 다른 기능들이 모여있는 라이브러리를 사용

# 표준 라이브러리
- 표준 라이브러리: 파이썬 설치할 때 같이 깔리는 기본 라이브러리

## datetime
- 연/월/일 관련 라이브러리

    ```py
    import datetime

    day1 = datetime.date(2021, 12, 13)
    day2 = datetime.date(2023, 4, 5)

    print(day1, day2)

    # datetime.date의 type
    print(type(day1))


    diff = day2 - day1

    # 두 날짜의 차이의 일수
    print(diff.days)

    ```
    ```
    2021-12-13 2023-04-05
    <class 'datetime.date'>
    478
    ```

## time
- 시간 관련 라이브러리

### time.time(): 현재 시간 반환
- utc 기반으로 1970년 1월 1일 0시 0분 0초 기준으로 몇 초가 지났는지 반환
    ```py
    import time

    print(time.time())
    ```
    ```
    1795073941.3957148
    ```

### time.sleep():
- time.sleep(int): int초만큼 딜레이
```py
import time

cnt = 0
while cnt < 5:
    cnt += 1
    print(cnt)
    time.sleep(1)
```
```
1
2
3
4
5
```
- 5초에 걸쳐 1초에 한줄씩 출력

## math
### math.gcd(a, b), math.lcm(a, b)
- 각각 a와 b의 최대공약수와 최소공배수를 반환

## random
- 난수 발생 모듈
### random.randint(a, b)
- a와 b사이의 정수 중 난수값 반환

```py
import random

for i in range(10):
    print(random.randint(1, 10), end=' ')
```
```
4 8 9 9 2 10 4 6 1 5 
```

## json
- json 파일을 다루는 라이브러리
- 파이썬은 json 라이브러리를 통해 딕셔너리로 다룸

    ```js
    //myinfo.json
    {"name" : "홍길동",
    "birth":"0525",
    "age":30}
    ```
    ```py
    # s6_5_json.py
    import json

    with open('./json/myinfo.json') as f:
        data = json.load(f)

    print(type(data))
    print(data)
    ```

### 딕셔너리를 json으로 바꾸기
```py
import json

d = {'name':'hong',
     'birth':'0525'}

json_data = json.dumps(d)
print(json_data)
print(type(json_data))
```
```
{"name": "hong", "birth": "0525"}
<class 'str'>
```

# 외부 라이브러리
- 외부 라이브러리는 따로 깔아야 함
- 설치 방법: 터미널에
    ```bash
    python -m pip install Somepackage
    ```
    입력

## numpy 설치
```bash
python -m pip install numpy

Collecting numpy
  Downloading numpy-2.5.5-cp315-cp315-win_amd64.whl.metadata (6.6 kB)
Downloading numpy-2.5.5-cp315-cp315-win_amd64.whl (12.7 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 12.7/12.7 MB 16.4 MB/s  0:00:00
Installing collected packages: numpy
  WARNING: The scripts f2py.exe and numpy-config.exe are installed in 'C:\Users\Admin\AppData\Local\Python\pythoncore-3.15-64\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed numpy-2.5.5

[notice] A new release of pip is available: 26.2.2 -> 26.3
[notice] To update, run: C:\Users\Admin\AppData\Local\Python\pythoncore-3.15-64\python.exe -m pip install --upgrade pip
```

- 정상적으로 설치되면 `Successfully installed numpy-2.5.5`가 뜸

### numpy 써보기
```py
import numpy as np

print(np.array([1, 2, 3]))
```
```
[1 2 3]
```

## numpy 삭제
```bash
python -m pip uninstall numpy

Found existing installation: numpy 2.5.5
Uninstalling numpy-2.5.5:
  Would remove:
    c:\users\admin\appdata\local\python\pythoncore-3.15-64\lib\site-packages\numpy-2.5.5.dist-info\*
    c:\users\admin\appdata\local\python\pythoncore-3.15-64\lib\site-packages\numpy.libs\libscipy_openblas64_-4e39871015dc1470c682dc512497ee22.dll
    c:\users\admin\appdata\local\python\pythoncore-3.15-64\lib\site-packages\numpy.libs\msvcp140-a4c2229bdc2a2a630acdc095b4d86008.dll
    c:\users\admin\appdata\local\python\pythoncore-3.15-64\lib\site-packages\numpy\*
    c:\users\admin\appdata\local\python\pythoncore-3.15-64\scripts\f2py.exe
    c:\users\admin\appdata\local\python\pythoncore-3.15-64\scripts\numpy-config.exe
Proceed (Y/n)? Y
  Successfully uninstalled numpy-2.5.5
```
- 라이브러리 삭제할 땐 uninstall 사용

### 삭제됬는지 확인
```py
import numpy as np

print(np.array([1, 2, 3]))
```
```
Traceback (most recent call last):
  File "c:\Users\Admin\Desktop\workspace\python_basic\day4\code\s6_library\s6_7_numpy.py", line 1, in <module>
    import numpy as np
ModuleNotFoundError: No module named 'numpy'. Did you mean: 'runpy'?
```
- 잘 삭제되서 라이브러리가 없어서 ModuleNotFoundError가 잘 뜸

## 설치된 라이브러리 조회
```bash
python -m pip list
Package Version
------- -------
numpy   2.5.5
pip     26.2.2
PS C:\Users\Admin\Desktop\workspace\python_basic\day4\code\s6_library> 
```