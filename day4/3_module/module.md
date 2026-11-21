# 모듈

- 모듈: 함수나 변수, 클래스를 모아놓은 파이선 파일
    - 다른 파이썬 프로그램에서 불러와 사용할 수 있게 만든 파이썬 파일

## 모듈 불러오기
```py
# cod3/s3/module/s3_1_module.py
def add(a, b):
    return a + b

def sub(a, b):
    return a - b
```
```py
# code/s3_module/s3_2_module_import.py
from s3_1_module import add, sub

print(add(1, 2))
print(sub(1, 2))
```
```
3
-1
```

### 기본 모듈
- math 모듈 불러와보기
```py
import math

print(math.pi)
print(math.sin(math.pi/2))
```
```
3.141592653589793
1.0
```