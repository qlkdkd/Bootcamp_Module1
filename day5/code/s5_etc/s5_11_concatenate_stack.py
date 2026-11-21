import numpy as np 

a = np.array([[1, 2], [3, 4]]) # 2 줄 2 칸 
b = np.array([[5, 6], [7, 8]]) # 2 줄 2 칸 

print(np.concatenate([a, b], axis=0).shape) # (4, 2) ← 아래로 이어 붙임 
print(np.concatenate([a, b], axis=1).shape) # (2, 4) ← 옆으로 이어 붙임 
print(np.stack([a, b]).shape) # (2, 2, 2) ← 두 장을 쌓음 

print(np.concatenate([a, b], axis=0))
print(np.concatenate([a, b], axis=1))
