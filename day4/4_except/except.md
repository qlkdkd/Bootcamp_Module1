# 예외처리
- 파이썬에는 ValueError, IndexError, SyntaxError 등 여러 오류가 있음
- ZeroDivisionError 예시
    ```py
    print(4/0)
    ```
    ```
    Traceback (most recent call last):
    File "c:\Users\Admin\Desktop\workspace\python_basic\day4\code\s4_except\s4_1_Error_example.py", line 1, in <module>
        print(4/0)
            ~^~
    ZeroDivisionError: division by zero
    ```

- 파이썬은 인터프리터 언어이기 때문에 한 줄에 오류가 나면 그 다음줄부턴 실행 불가능, 중단되버림

## 오류 예외처리 기법

### try-except 문
```py
try:
    #우리가 시도하려는 코드
except [발생 오류[as 변수]]:
    # try에서 오류가 발생하면 진입
```
- try 블록 수행 중 오류가 발생되면 except 블록이 수행됨

#### try-except 예제
    ```py
    try: # 에러가 우려되는 코드
        a = [1, 2, 3]
        a[3] # Error!
        print('try1'); print('try2')
    except:
        print('오류 발생')
    ```
    ```
    오류 발생
    ```
- a[3]에서 오류 발생
    - except로 건너가 '오류 발생' 메시지 출력
- try문 내부의 오류발생지점 이후 코드는 실행되지 않음


## finally
- try문 도중 수행 도중 예외 발생 여부에 상관없이 항상 수행됨\
    ```py
    # try_finally2.py
    try:
        print("나누기 전")
        4 / 0
        print("나누기 후")
    except ZeroDivisionError:
        print("오류가 발생했습니다.")
    finally:
        print("finally 실행!")
    ```
    ```
    나누기 전
    오류가 발생했습니다.
    finally 실행!
    ```
- 위 예제에서 4 / 0에서 에러 발생 후 except문이 실행되고, finally문이 실행되미