import numpy as np 
v = np.array([1, 2, 3]) 
print(v.shape) # (3,) 
print(v[:, np.newaxis].shape) # (3, 1) ← 세로로 세움 
print(v[np.newaxis, :].shape) # (1, 3) ← 가로 한 줄짜리 표 
