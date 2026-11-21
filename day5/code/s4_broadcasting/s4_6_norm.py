import numpy as np 

p1 = np.array([100, 200]) 
p2 = np.array([400, 600]) 
print(np.linalg.norm(p2 - p1)) # 500.0 ← 두 점 사이 직선 거리 
