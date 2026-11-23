import numpy as np 
import pandas as pd 


df = pd.DataFrame({ 
    "label": ["person", "car", "person", "helmet", "car"], 
    "conf": [0.91, np.nan, 0.42, 0.85, np.nan], 
    "latency_ms": [32.5, 41.2, np.nan, 30.1, 44.7], 
}) 

print('---drop_all---')
print(df.dropna()) # 빈 칸이 하나라도 있는 줄을 지움 → 2 줄 남음 

print('---drop conf---')
print(df.dropna(subset=["conf"])) # conf 가 빈 줄만 지움 → 3 줄 남음 


# 원본 건들지 않기 위해 따로 copy
filled = df.copy() 
filled["latency_ms"] = filled["latency_ms"].fillna(filled["latency_ms"].median()) #  가운데값으로 채우기 
filled["conf"] = filled["conf"].fillna(0) #  0 으로 채우기 
print('---fill latency_ms to mean and conf to 0---')
print(filled) 
