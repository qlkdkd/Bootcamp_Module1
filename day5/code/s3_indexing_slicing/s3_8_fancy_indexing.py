import numpy as np 


a = np.array([10, 20, 30, 40, 50]) 
print(a[[0, 2, 4]]) # [10 30 50] 
print(a[[4, 0]]) # [50 10] ← 순서도 목록대로 

b = np.arange(1, 13).reshape(3, 4) 
print(b[[0, 2]]) # 0 번 줄과 2 번 줄 
