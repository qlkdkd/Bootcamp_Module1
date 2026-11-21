import numpy as np 

prod = np.array([
    [80, 90, 70, 60], 
    [95, 85, 75, 65], 
    [70, 60, 90, 80]]) # 라인 3 개 × 요일 4 일

print(prod.mean().round(1)) # 76.7 ← 방향 없이 전체 평균 
print(prod.mean(axis=0).round(1)) # [81.7 78.3 78.3 68.3] ← 요일별 평균 (4 개) 
print(prod.mean(axis=1)) # [75. 80. 75.] ← 라인별 평균 (3 개) 
