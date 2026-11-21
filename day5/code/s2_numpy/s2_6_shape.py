import numpy as np 


b = np.array([
    [1, 2, 3], 
    [4, 5, 6]
]) 

print(b.shape) # (2, 3) ← 2 줄 3 칸 
print(b.ndim) # 2 ← 방향이 몇 개인가 (줄, 칸 → 2 개) 
print(b.size) # 6 ← 칸이 모두 몇 개인가 
print(b.dtype) # int64 ← 칸에 든 숫자의 종류 
