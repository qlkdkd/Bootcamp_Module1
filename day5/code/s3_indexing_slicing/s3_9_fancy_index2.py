import numpy as np 


conf = np.array([0.91, 0.32, 0.77]) 
names = np.array(["person", "car", "dog"]) 


order = np.argsort(conf)[::-1] # 큰 것부터의 번호 순서 

print(order) # [0 2 1] 
print(conf[order]) # [0.91 0.77 0.32] 
print(names[order]) # ['person' 'dog' 'car'] ← 이름도 같은 순서로
