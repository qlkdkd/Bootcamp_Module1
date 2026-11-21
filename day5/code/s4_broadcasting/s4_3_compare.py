import numpy as np 

temp = np.array([36.5, 37.2, 38.1, 36.9]) # 측정 온도 4 개 

# 37.5보다 큰가?
print(temp > 37.5) # [False False True False] 

# 하나라도 37.5보다 큰가?
print((temp > 37.5).any()) # True 

# 전부 40도 미만인가?
print((temp < 40).all()) # True

if (temp > 37.5).any(): # if 에는 True/False 하나만 들어갈 수 있다  
    print("기준 초과 값 있음") 