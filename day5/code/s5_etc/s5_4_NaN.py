import numpy as np 

d = np.array([1.2, np.nan, 3.4, 2.0]) 

print(d.mean()) # nan ← 빈 값 때문에 계산 불가 
print(np.nanmean(d)) # 2.2 ← 빈 값을 빼고 평균 
print(np.isnan(d)) # [False True False False] ← 어느 칸이 비었나 
print(d[~np.isnan(d)]) # [1.2 3.4 2. ] ← 빈 칸 빼고 남기기 
print(np.nan == np.nan) # False ← NaN 은 == 로 확인할 수 없다
