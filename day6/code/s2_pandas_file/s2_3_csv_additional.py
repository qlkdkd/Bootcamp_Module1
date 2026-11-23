import os 
import pandas as pd 

root = r'C:\Users\Admin\Desktop\workspace\python_basic\day6\code\s2_pandas_file\data'

os.makedirs(root, exist_ok=True) 

df = pd.DataFrame(
    {"label": ["사람", "차량"], 
     "conf": [0.91, 0.77]}) 

df.to_csv(
    root + r"\with_index.csv", 
    encoding="utf-8") # index=False 를 빼먹으면


print(pd.read_csv(
    root + r"\with_index.csv", encoding="utf-8")
) 


# Unnamed: 0 label conf ← 줄 이름표가 이상한 열로 따라 들어옴 
df.to_csv(
    root + r"/for_excel.csv", 
    index=False, 
    encoding="utf-8-sig"
) # 엑셀에서 열 한글 CSV 
print("저장 완료") 
