import numpy as np 
import matplotlib.pyplot as plt

H, W = 200, 300 
img = np.zeros((H, W, 3), dtype=np.uint8) # 검은 바탕 (모두 0) 


img[:, :100] = [255, 0, 0] # 왼쪽 영역 → 빨강 
img[:, 100:200] = [0, 255, 0] # 가운데 → 초록 
img[:, 200:] = [0, 0, 255] # 오른쪽 → 파랑 

img[80:120, 130:170] = 255 # 가운데 작은 네모 → 흰색 (세 값 모두 255) 

print(img.shape) # (200, 300, 3) 
print(img[100, 50]) # [255 0 0] ← y=100, x=50 픽셀은 빨강 
print(img[100, 150]) # [255 255 255] ← 가운데 네모는 흰색 
plt.imshow(img) 
plt.show() 