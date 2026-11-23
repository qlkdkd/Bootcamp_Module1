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