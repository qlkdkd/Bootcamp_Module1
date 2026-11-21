import numpy as np 

rng = np.random.default_rng(0) 

gray = rng.integers(0, 256, size=(4, 4)) # 밝기 0~255 인 작은 사진 print(gray) 

# 원본을 해치지 않기 위해 카피
binary = gray.copy() 


# 128보다 크면 흰색, 아니면 검은색
binary[gray >= 128] = 255 # 밝은 칸 → 흰색 
binary[gray < 128] = 0 # 어두운 칸 → 검은색 
print(binary) 


# 한 줄 버전: np.where(조건, 맞으면 이 값, 틀리면 이 값) 
binary2 = np.where(gray >= 128, 255, 0) 
print((binary == binary2).all()) # True ← 두 방법의 결과가 같다 