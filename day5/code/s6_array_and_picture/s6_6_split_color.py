import numpy as np 
import matplotlib.pyplot as plt 


H, W = 240, 320 
y = np.linspace(0, 1, H)[:, np.newaxis] 
x = np.linspace(0, 1, W)[np.newaxis, :] 

img = np.zeros((H, W, 3)) 
img[:, :, 0], img[:, :, 1], img[:, :, 2] = x, y, 0.5 
img = (img * 255).astype(np.uint8) 

R = img[:, :, 0] # 빨강 판만 (높이, 너비) 
G = img[:, :, 1] # 초록 판만 
B = img[:, :, 2] # 파랑 판만 

print(R.shape) # (240, 320) 


# 흑백 만들기 ①: 세 값의 평균 (4 장의 axis) 
gray_avg = img.mean(axis=2) 


# 흑백 만들기 ②: 사람 눈에 맞춘 방법. 사람은 초록을 가장 밝게 느끼므로 비중을 다르게 
gray = img @ np.array([0.299, 0.587, 0.114]) # 칸마다 빨×0.299 + 초×0.587 +  파×0.114 (3-1 의 @) 
gray = gray.astype(np.uint8) 


print(gray.shape, gray.dtype) # (240, 320) uint8 
fig, axes = plt.subplots(1, 3, figsize=(12, 3)) 
axes[0].imshow(img) 
axes[1].imshow(R, cmap="gray") # 빨강 판을 밝기로 보기 
axes[2].imshow(gray, cmap="gray") # 흑백은 cmap="gray"를 꼭 적는다 

plt.savefig('./data/color_split.jpg')
plt.show() 
