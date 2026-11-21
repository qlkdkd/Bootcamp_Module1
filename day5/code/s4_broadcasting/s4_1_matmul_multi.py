import numpy as np 


qty = np.array([
    [2, 1], # 제품 1 
    [1, 3], # 제품 2 
    [0, 2]]) # 제품 3
 
price = np.array([3000, 2000]) 

print(qty @ price) # [8000 9000 4000] ← 제품별 원가 
