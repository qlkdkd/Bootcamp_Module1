import numpy as np 

c = np.zeros((4, 4), dtype=int) 

c[1:3, 1:3] = 9 # 가운데 2×2 영역을 9 로 채우기 
c[0, :] = 1 # 맨 윗줄을 1 로 
print(c) 
# [[1 1 1 1] 
# [0 9 9 0] 
# [0 9 9 0] 
# [0 0 0 0]] 
