import numpy as np 


a = np.array([1, 2, 3]) # 한 줄짜리 
b = np.array([[1, 2, 3], [4, 5, 6]]) # 2 줄 3 칸짜리 

print(a) 
print(b) 

print(np.zeros((2, 3))) # 0 으로 채운 2 줄 3 칸

print(np.ones((2, 3))) # 1 로 채운 2 줄 3 칸 

print(np.full((2, 3), 7)) # 7 로 채운 2 줄 3 칸 

print(np.arange(0, 10, 2)) # [0 2 4 6 8] 0 부터 2 씩, 10 직전까지 
print(np.linspace(0, 1, 5)) # [0. 0.25 0.5 0.75 1. ] 0 과 1 사이를 5 개 값으로 고르게 
