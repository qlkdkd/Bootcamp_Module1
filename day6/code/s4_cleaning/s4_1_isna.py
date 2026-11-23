import numpy as np 
import pandas as pd 

df = pd.DataFrame({ 
    "label": ["person", "car", "person", "helmet", "car"], 
    "conf": [0.91, np.nan, 0.42, 0.85, np.nan], 
    "latency_ms": [32.5, 41.2, np.nan, 30.1, 44.7], 
}) 

print('isna')
print(df.isna()) # 칸마다 비었으면 True 
print()

print('isna.sum()')
print(df.isna().sum()) # 열마다 빈 칸 개수: label 0, conf 2, latency_ms 1 
print()

print('isna.mean()')
print(df.isna().mean()) # 열마다 빈 칸 비율: conf 0.4 (40%)
print()

print('isna.any(axis=1)')
print(df[df.isna().any(axis=1)]) # 빈 칸이 하나라도 있는 줄 
