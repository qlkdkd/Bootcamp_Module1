import pandas as pd 

df = pd.DataFrame({ 
    "time": ["2026-11-20 09:00:01", "2026-11-20 09:00:03", "2026-11-20 09:00:04"],  
    "count": ["12", "-", "3"], 
    "camera": ["cam1", "cam2", "cam1"], 
}) 

print('---incorrext df---')
print(df.dtypes) # 세 열 모두 글자(str) 
print(df['count'].sum()) # 12-3('12' + 'NaN' + '3')


# 타입 수정
df["time"] = pd.to_datetime(df["time"]) # 글자 → 날짜 
df["count"] = pd.to_numeric(df["count"], errors="coerce") # 글자 → 숫자 (못 바꾸는 값은 빈 칸) 
df["camera"] = df["camera"].astype("category") # 몇 가지 값만 반복되는 열 → 범주형 (메모리 절약) 

print('--modify to check incorrect data types')
print(df.dtypes) # time: datetime, count: float64,  camera: category 

print('---modified dataframe---')
print(df) 
print(df["count"].sum()) # 15.0 ← 이제 계산이 된다
