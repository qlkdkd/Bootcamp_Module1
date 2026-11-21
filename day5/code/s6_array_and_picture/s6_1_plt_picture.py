import numpy as np 
import matplotlib.pyplot as plt 

gray = np.array([
    [ 0, 50, 100, 150],
    [ 50, 100, 150, 200], 
    [100, 150, 200, 250], 
    [150, 200, 250, 255]], 
    dtype=np.uint8
) 

print(gray.shape, gray.dtype) # (4, 4) uint8 
print(gray[0, 0], gray[3, 3]) # 0 255 ← 왼쪽 위가 가장 어둡고 오른쪽 아래가 가장 밝다 

plt.imshow(gray, cmap="gray", vmin=0, vmax=255) # 숫자를 밝기로 그려서 보여주기 
plt.colorbar() # 오른쪽에 숫자-밝기 대응표 plt.show() 
plt.show()