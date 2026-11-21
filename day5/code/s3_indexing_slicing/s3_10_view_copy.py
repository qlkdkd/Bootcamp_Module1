import numpy as np 

a = np.array([1, 2, 3, 4, 5]) 


v = a[1:4] # 창(view) 
v[0] = 99 
print(a) # [ 1 99 3 4 5] ← 원본이 바뀜! 


c = a[1:4].copy() # 사본(copy) 
c[0] = 0 
print(a) # [ 1 99 3 4 5] ← 원본은 그대로 
print(c) # [ 0 3 4] 
