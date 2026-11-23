import pandas as pd 
count = pd.Series(
    [12, 5, 3], 
    index=["person", "car", "dog"]
) 

print(count) 
print(count["car"]) # 5 ← 이름표로 찾기 
print(count[count > 4]) # person 12, car 5 ← NumPy 와 같은 조건 고르기 print(count * 2) # 칸마다 계산도 그대로 
print(count.sum()) # 20 
print(count.to_numpy()) # [12 5 3] ← 이름표를 떼면 NumPy 배열
