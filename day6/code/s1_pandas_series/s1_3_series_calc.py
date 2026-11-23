import pandas as pd 
mon = pd.Series({"person": 12, "car": 5, "dog": 3}) 
tue = pd.Series({"car": 7, "person": 10, "bike": 2}) 
print(mon + tue) 
print()
# bike NaN ← 월요일엔 없음 
# car 12.0 ← 5 + 7 
# dog NaN ← 화요일엔 없음 
# person 22.0 ← 12 + 10 
print(mon.add(tue, fill_value=0)) # 짝이 없으면 0 으로 보고 더하기 
