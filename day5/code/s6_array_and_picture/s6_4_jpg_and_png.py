import os 
import numpy as np 
import matplotlib.pyplot as plt 

os.makedirs("data", exist_ok=True) 
plt.imsave("data/test.png", np.full((100, 150, 3), 200, dtype=np.uint8)) 

img = plt.imread("data/test.png") 
print("읽은 직후:", img.shape, img.dtype) # (100, 150, 4) float32 

if img.dtype != np.uint8: # 0~1 소수라면 
    img = (img * 255).round().astype(np.uint8) # 0~255 정수로 

img = img[:, :, :3] # 투명도가 있으면 빼고 색 3 개만 
print("맞춘 뒤:", img.shape, img.dtype) # (100, 150, 3) uint8 
print(img[0, 0]) # [200 200 200] 
