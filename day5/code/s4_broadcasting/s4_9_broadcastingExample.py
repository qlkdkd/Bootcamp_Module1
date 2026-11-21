import numpy as np 

points = np.array([[100, 200], [300, 400], [50, 60]]) # 찾은 물체 3 개의 중심 
center = np.array([320, 240]) # 화면 가운데 
dist = np.linalg.norm(points - center, axis=1) # 각 점에서 가운데까지 거리 

print(dist.round(1)) # [223.6 161.2 324.5] 
print(points[np.argmin(dist)]) # [300 400] ← 가운데에 가장 가까운 물체 
