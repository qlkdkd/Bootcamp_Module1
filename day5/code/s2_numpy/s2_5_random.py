import numpy as np 


rng = np.random.default_rng(seed=42) 

print(rng.integers(0, 256, size=(2, 3))) # 0~255 사이 정수 (사진 밝기 범위) 
print(rng.random((2, 3))) # 0~1 사이 실수 
print(rng.normal(0, 1, size=5)) # 0 근처에 몰린 값 5 개 (센서 잡음을 흉내낼 때) 