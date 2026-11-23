import os 
import pandas as pd 

root = r'C:\Users\Admin\Desktop\workspace\python_basic\day6\code\s2_pandas_file\data'
os.makedirs(root, exist_ok=True) 

cams = pd.DataFrame({ 
    "camera": ["cam1", "cam2"], 
    "location": ["입구", "작업장"], 
    "resolution": ["640x480", "1280x720"],
}) 

cams.to_json(
    root + r"\cameras.json", 
    orient="records", 
    force_ascii=False, 
    indent=2
)

with open(root + r"\cameras.json", encoding="utf-8") as f: 
    print(f.read()) 
# [ 
# { 
# "camera":"cam1", 
# "location":"입구", 
# ... 
print(pd.read_json(root + r'\cameras.json')) 
