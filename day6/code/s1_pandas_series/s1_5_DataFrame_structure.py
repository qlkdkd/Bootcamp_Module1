import pandas as pd 

df = pd.DataFrame({ 
 "frame": [1, 1, 2, 3, 3], 
 "label": ["person", "car", "person", "dog", "person"], 
 "conf": [0.91, 0.77, 0.85, 0.42, 0.66], 
}) 

print('크기:', df.shape) # (5, 3) ← 5 줄 3 칸 
print('열 목록:', df.columns.tolist()) # ['frame', 'label', 'conf'] ← 열 이름(머리글) 
print('행 목록:', df.index.tolist()) # [0, 1, 2, 3, 4] ← 줄 이름표 
print('열들의 타입\n', df.dtypes) # 열마다 값의 종류 
print('df[\'conf\']\n', df["conf"],  '\n') # 열 하나 꺼내기 → Series 
print('df[\'conf\'] (넘파이 변환)\n',df["conf"].to_numpy()) # [0.91 0.77 0.85 0.42 0.66] ← NumPy 배열로
