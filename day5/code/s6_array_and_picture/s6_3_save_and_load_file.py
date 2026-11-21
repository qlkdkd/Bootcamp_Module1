import os 
import numpy as np 
import matplotlib.pyplot as plt 

os.makedirs("data", exist_ok=True) 

img = np.zeros((100, 150, 3), dtype=np.uint8) 
img[:, :75] = [255, 128, 0] # 왼쪽 절반 주황 

plt.imsave("data/test.png", img) # 배열 → 사진 파일 
loaded = plt.imread("data/test.png") # 사진 파일 → 배열 

print(loaded.shape, loaded.dtype) # (100, 150, 4) float32 
print(loaded[0, 0]) # [1. 0.5 0. 1. ] 근처 값
