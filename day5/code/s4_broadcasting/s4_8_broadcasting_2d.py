import numpy as np

M = np.array([
    [1, 2, 3], 
    [4, 5, 6]]) # 2 줄 3 칸 


row = np.array([10, 20, 30]) # 가로 한 줄 → 모든 줄에 적용 
print(M + row) 
# [[11 22 33] 
# [14 25 36]] 


col = np.array([
    [100], 
    [200]]) # 세로 한 줄 → 모든 칸에 적용 

print(M + col) 
# [[101 102 103] 
