import numpy as np 
import pandas as pd 

df = pd.DataFrame({ 
    "label": ["person", "helmet", "car", "person"], 
    "conf": [0.91, 0.85, 0.77, 0.38], 
    "x1": [120, 130, 300, 50], "y1": [80, 70, 200, 60], 
    "x2": [180, 170, 460, 90], "y2": [240, 110, 300, 200], 
    "latency_ms": [32.5, 32.5, 47.2, 38.0], 
}) 

print('original')
print(df);print()

pd.set_option("display.max_columns", None) # 열이 많아도 생략(...) 없이 모두 출력 
pd.set_option("display.width", 200) 

df["w"] = df["x2"] - df["x1"] # 상자 너비 
df["h"] = df["y2"] - df["y1"] # 상자 높이 
df["area"] = df["w"] * df["h"] # 상자 넓이 
df["is_slow"] = df["latency_ms"] > 45 # 느렸는지 True/False 
df["level"] = np.where(df["conf"] >= 0.8, "high", "low") # np.where(조건, 맞으면,  틀리면) 
df.loc[df["conf"] < 0.4, "level"] = "reject" # 조건에 맞는 줄만 값 바꾸기 — 반드시 loc 으로 


print('added w, h, area, is_slow & drop w, h & rename latency_ms to latency')
print(df) 

df = df.drop(columns=["w", "h"]) # 열 지우기 
df = df.rename(columns={"latency_ms": "latency"}) # 열 이름 바꾸기 
print(df.columns.tolist()) 
# ['label', 'conf', 'x1', 'y1', 'x2', 'y2', 'latency', 'area', 'is_slow', 'level'] 
