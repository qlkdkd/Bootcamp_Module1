import numpy as np 

a = np.arange(12) # [ 0 1 2 ... 11] 한 줄에 12 개 print(a) 

print(a.reshape(3, 4)) # 3 줄 4 칸 
print(a.reshape(2, 6)) # 2 줄 6 칸 
print(a.reshape(-1, 6).shape) # (2, 6) ← -1 은 "나머지는 알아서 맞춰줘" print(a.reshape(-1, 1).shape) # (12, 1) ← 세로로 길게 한 줄

try: 
    a.reshape(5, 2) 
except ValueError as e: 
    print("에러:", e) # 12 개를 10 칸에 못 담음 
