import time 
import numpy as np 

n = 1_000_000 # 100 만 (밑줄은 읽기 편하게 넣은 것, 숫자에 영향 없음) 
lst = list(range(n)) 
arr = np.arange(n) 
t = time.perf_counter()


r1 = [x ** 2 for x in lst] # 하나씩 제곱 
t_list = time.perf_counter() - t 
t = time.perf_counter() 


r2 = arr ** 2 # 통째로 제곱 
t_np = time.perf_counter() - t 


print(f"리스트: {t_list:.4f}초") 
print(f"NumPy : {t_np:.4f}초") 
print(f"약 {t_list / t_np:.0f}배 차이") 