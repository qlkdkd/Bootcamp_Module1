# 데이터 읽기

import pandas as pd

root = r'C:\Users\Admin\Desktop\workspace\python_basic\day6\code\s2_pandas_file\vision_inspection_log.csv'
df = pd.read_csv(root)

print(df.head())
print(df.info())
print(df.describe())
