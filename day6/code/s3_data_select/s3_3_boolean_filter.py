import pandas as pd 

df = pd.DataFrame({ 
 "camera": ["cam1", "cam1", "cam2", "cam2", "cam1", "cam2", "cam1", "cam2"],  
 "label": ["person", "helmet", "car", "person", "forklift", "person", "helmet",  "car"], 
 "conf": [0.91, 0.85, 0.77, 0.42, 0.66, 0.88, 0.58, 0.95], 
 "latency_ms": [32.5, 32.5, 41.2, 38.0, 29.8, 47.3, 30.1, 44.7], }) 


high = df[df["conf"] >= 0.8] # 신뢰도 0.8 이상인 줄만 print(high) 
print(len(high)) # 4 


mask = (df["label"] == "person") & (df["camera"] == "cam2") 
print(df[mask]) # cam2 가 찾은 person 
print(df[df["label"].isin(["car", "forklift"])]) # car 또는 forklift 인 줄 

print(df[df["latency_ms"].between(30, 40)]) # 30 이상 40 이하인 줄 

print(df.loc[df["conf"] >= 0.9, ["label", "conf"]]) # 조건과 열을 한 번에: loc[조건,  열] 

print(df.query("label == 'person' and conf >= 0.8")) # 조건을 문장처럼 쓰기