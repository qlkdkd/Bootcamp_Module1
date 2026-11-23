import os 
import pandas as pd 


root = r'C:\Users\Admin\Desktop\workspace\python_basic\day6\code\s2_pandas_file'

os.makedirs(root + r"\data", exist_ok=True) # data 폴더가 없으면 만들기 

df = pd.DataFrame({
 "time": ["2026-11-20 09:00:01", "2026-11-20 09:00:03", "2026-11-20 09:00:04"],  
 "camera": ["cam1", "cam2", "cam2"], 
 "label": ["person", "car", "person"], 
 "conf": [0.91, 0.77, 0.42], 
}) 


new_root = root + r'\data\sample.csv'
df.to_csv(new_root, index=False, encoding="utf-8") # 저장 


with open(new_root, encoding="utf-8") as f: # 파일 안이 어떻게 생겼는지 직접 보기 
    print(f.read()) 
# time,camera,label,conf 
# 2026-11-20 09:00:01,cam1,person,0.91 
# ... 
loaded = pd.read_csv(new_root, encoding="utf-8") # 다시 읽기 print(loaded) 
print(loaded.dtypes) # time 이 글자(str)로 읽혔다 
