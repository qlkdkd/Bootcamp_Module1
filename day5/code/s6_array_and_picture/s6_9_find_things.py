import numpy as np 
import matplotlib.pyplot as plt 


# 테스트 장면: 회색 배경에 빨간 네모 하나 
scene = np.full((240, 320, 3), 120, dtype=np.uint8) 
scene[60:140, 180:260] = [220, 30, 30] 

R = scene[:, :, 0].astype(int) 
G = scene[:, :, 1].astype(int) 
B = scene[:, :, 2].astype(int) 

red_mask = (R > 150) & (G < 80) & (B < 80) # ① 마스크: 빨강은 강하고 나머지는 약한 픽셀 

print("빨간 픽셀 수:", red_mask.sum()) # 6400 (80×80) 


ys, xs = np.nonzero(red_mask) # ② 조건에 맞는 픽셀들의 y, x 위치 목록 

x1, y1, x2, y2 = int(xs.min()), int(ys.min()), int(xs.max()), int(ys.max()) 

cx, cy = float(xs.mean()), float(ys.mean()) 

print("둘러싼 상자:", (x1, y1, x2, y2)) # (180, 60, 259, 139) 
print("중심점:", (cx, cy)) # (219.5, 99.5) 


result = scene.copy() 
result[~red_mask] = result[~red_mask] // 3 # ③ 빨간 부분 밖은 어둡게 

fig, axes = plt.subplots(1, 3, figsize=(12, 3)) 
axes[0].imshow(scene) 
axes[1].imshow(red_mask, cmap="gray") # 조건에 맞는 부분 (흰색) 
axes[2].imshow(result) 
axes[2].plot(cx, cy, "y+", markersize=15) # 중심점에 노란 + 표시 

plt.savefig('./data/finded.jpg')
plt.show() 
