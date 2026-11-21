import numpy as np 
import matplotlib.pyplot as plt 


def adjust(img, brightness=0, contrast=1.0): 
    out = img.astype(np.float32) * contrast + brightness # ① 소수로 계산  
    out = np.clip(out, 0, 255) # ② 0~255 안으로 자르기  
    return out.astype(np.uint8) # ③ 다시 uint8 


# 그라데이션 사진 
H, W = 240, 320 
y = np.linspace(0, 1, H)[:, np.newaxis] 
x = np.linspace(0, 1, W)[np.newaxis, :] 
img = np.zeros((H, W, 3)) 

img[:, :, 0], img[:, :, 1], img[:, :, 2] = x, y, 0.5 
img = (img * 255).astype(np.uint8) 
bright = adjust(img, brightness=80) # 밝게 
dark = adjust(img, brightness=-80) # 어둡게 
high_c = adjust(img, contrast=1.8, brightness=-100) # 대비 강하게 (밝은 곳은 더 밝게,  어두운 곳은 더 어둡게) 

wrong = img + 80 # 잘못된 방법 → 밝은 부분이 어두워짐 


print("원본 최댓값:", img.max()) # 255 
print("bright 최댓값:", bright.max()) # 255 ← 255 에서 멈춤 
print("wrong 최솟값:", wrong.min()) # 0 ← 되돌아간 픽셀이 생김 


fig, axes = plt.subplots(1, 4, figsize=(12, 3)) 
for ax, im, t in zip(
    axes, 
    [bright, dark, high_c, wrong], 
    ["bright", "dark", "contrast", "overflow!"]):  
    ax.imshow(im) 
    ax.set_title(t) 

plt.savefig('./overflow_data.jpg')
plt.show() 
