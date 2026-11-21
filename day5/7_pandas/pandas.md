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