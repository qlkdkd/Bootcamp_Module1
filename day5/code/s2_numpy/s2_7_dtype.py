import numpy as np 


img = np.zeros((480, 640, 3), dtype=np.uint8) # 만들 때 종류를 정해주기 

print(img.dtype, img.nbytes) # uint8 921600 ← 약 0.9MB 

f = img.astype(np.float32) # 종류 바꾸기 

print(f.dtype, f.nbytes) # float32 3686400 ← 4 배로 커짐 
