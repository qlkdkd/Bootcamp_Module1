import numpy as np 
import matplotlib.pyplot as plt 

# 그라데이션 사진 만들기 (브로드캐스팅 활용) 
H, W = 240, 320 
y = np.linspace(0, 1, H)[:, np.newaxis] # 위→아래로 0→1 (세로 한 줄) 
x = np.linspace(0, 1, W)[np.newaxis, :] # 왼→오른쪽으로 0→1 (가로 한 줄) 
img = np.zeros((H, W, 3)) 

img[:, :, 0] = x # 빨강: 오른쪽으로 갈수록 강해짐 
img[:, :, 1] = y # 초록: 아래로 갈수록 강해짐 
img[:, :, 2] = 0.5 # 파랑: 전체에 절반 
img = (img * 255).astype(np.uint8) 

crop = img[50:150, 100:250] # 자르기: y 50~149, x 100~249 영역 

flip_lr = img[:, ::-1] # 좌우 뒤집기 (가로를 거꾸로) 
flip_ud = img[::-1, :] # 위아래 뒤집기 
small = img[::2, ::2] # 한 칸씩 건너뛰기 → 가로·세로 절반 크기 
rot90 = np.rot90(img) # 왼쪽으로 90 도 돌리기 


for name, im in [
    ("원본", img), ("crop", crop), 
    ("flip", flip_lr), ("half", small),  
    ("rot90", rot90)]: 

    print(name, im.shape)


fig, axes = plt.subplots(1, 5, figsize=(15, 3)) # 그림 5 개를 나란히 
for ax, im, title in zip(
    axes, 
    [img, crop, flip_lr, small, rot90],  
    ["original", "crop", "flip", "half", "rot90"]
    ):  
    
    ax.imshow(im) 
    ax.set_title(f"{title} {im.shape}") 

plt.savefig('./data/cutting_slicing.jpg')
plt.show() 
