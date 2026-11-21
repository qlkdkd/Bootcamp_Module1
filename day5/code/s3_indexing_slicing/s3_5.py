import numpy as np 

conf = np.array([0.91, 0.32, 0.77, 0.15, 0.58]) # AI 가 낸 신뢰도 

mask = conf >= 0.5 # ① 판정표 만들기 


print(mask) # [ True False True False True] 
print(conf[mask]) # ② 통과한 것만: [0.91 0.77 0.58] 
print(mask.sum()) # 3 ← True 는 1 로 세어지므로 '통과한 개수'가 된다
