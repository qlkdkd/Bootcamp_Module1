import numpy as np 
import pandas as pd 

s = pd.Series([1.0, np.nan, np.nan, 4.0]) 

print(s.ffill().tolist()) # [1.0, 1.0, 1.0, 4.0] ← 바로 앞의 값을 그대로 이어쓰기 
print(s.interpolate().tolist()) # [1.0, 2.0, 3.0, 4.0] ← 앞뒤 값 사이를 고르게 채우기 
