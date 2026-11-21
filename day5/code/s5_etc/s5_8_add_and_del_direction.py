import numpy as np 

img = np.zeros((3, 480, 640)) 

batch = img[np.newaxis] # 맨 앞에 크기 1 인 방향 추가 
print(batch.shape) # (1, 3, 480, 640) 

out = np.zeros((1, 5, 6)) # 모델 결과도 1 장짜리 묶음에 담겨 나옴 
print(out[0].shape) # (5, 6) ← 0 번째 꺼내기 

print(out.squeeze().shape) # (5, 6) ← 크기 1 인 방향을 모두 없애기