import numpy as np 


x = np.array([-4.7, -1.2, 0.0, 2.5, 9.0]) 

print(np.abs(x)) # [4.7 1.2 0. 2.5 9. ] ← 부호 떼기 
print(np.round(x)) # [-5. -1. 0. 2. 9.] ← 반올림 (.5 는 짝수 쪽으로) 
print(np.floor(x)) # [-5. -2. 0. 2. 9.] ← 내림 
print(np.ceil(x)) # [-4. -1. 0. 3. 9.] ← 올림 
print(np.clip(x, 0, 5)) # [0. 0. 0. 2.5 5. ] ← 0 보다 작으면 0, 5 보다 크면 5 로
