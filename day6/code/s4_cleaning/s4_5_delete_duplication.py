import pandas as pd

df = pd.DataFrame({ 
    "time": ["09:00:01", "09:00:01", "09:00:03", "09:00:03"], 
    "camera": ["cam1", "cam1", "cam2", "cam2"], 
    "label": ["person", "person", "car", "car"], 
    "conf": [0.91, 0.91, 0.77, 0.79], 
}) 

print('---duplicated list---')
print(df.duplicated()) # 앞에 똑같은 줄이 있으면 True 

print('---duplicated count')
print(df.duplicated().sum()) # 1 ← 완전히 똑같은 줄 수 

print('---drop duplicated---')
print(df.drop_duplicates()) # 4 줄 → 3 줄 

print('---drop subset duplicated---')
print(df.drop_duplicates(subset=["time", "camera", "label"])) # 이 세 열만 같아도 중복으로 보기 → 2 줄 
