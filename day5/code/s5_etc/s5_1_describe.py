import numpy as np 

x = np.array([3, 7, 1, 9, 4]) 
print(x.sum()) # 24 합계 
print(x.mean()) # 4.8 평균 
print(x.min()) # 1 가장 작은 값
print(x.max()) # 9 가장 큰 값 
print(x.argmin()) # 2 가장 작은 값이 있는 자리(번호) 
print(x.argmax()) # 3 가장 큰 값이 있는 자리(번호) 
print(np.median(x)) # 4.0 줄 세웠을 때 가운데 값 
print(x.std().round(2)) # 2.86 표준편차: 값들이 평균에서 평균적으로 얼마나 떨어져 있는지 
