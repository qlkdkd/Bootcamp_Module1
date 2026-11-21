import numpy as np 

qty = np.array([2, 1]) # 부품 수량: A 2 개, B 1 개 
price = np.array([3000, 2000]) # 부품 단가: A 3000 원, B 2000 원 
print(qty * price) # [6000 2000] ← 곱하기만 함 (부품별 금액) 
print((qty * price).sum()) # 8000 ← 곱하고 더하기 
print(qty @ price) # 8000 ← 위와 같은 계산을 한 번에
