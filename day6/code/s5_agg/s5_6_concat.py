import os 
import pandas as pd


part1 = pd.DataFrame({
    "label": ["person", "car"], 
    "conf": [0.91, 0.77]}) 

part2 = pd.DataFrame({
    "label": ["helmet"], 
    "conf": [0.85]})
 
print(pd.concat([part1, part2])) # 이름표가 0, 1, 0 으로 겹침 print(pd.concat([part1, part2], ignore_index=True)) # 이름표를 0, 1, 2 로 새로 
# 폴더에 있는 CSV 여러 개를 한 번에 읽어서 잇기 

root = r'C:\Users\Admin\Desktop\workspace\python_basic\day6\code\s5_agg\data'

os.makedirs("data", exist_ok=True) 

part1.to_csv(root + r'\log1.csv', index=False, encoding="utf-8") 
part2.to_csv("data/log_02.csv", index=False, encoding="utf-8") 

from pathlib import Path 
files = sorted(Path("data").glob("log_*.csv")) # log_로 시작하는 CSV 파일 목록 print(files) 
logs = pd.concat([pd.read_csv(f, encoding="utf-8") for f in files], ignore_index=True) 
print(logs) 
