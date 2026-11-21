import numpy as np 

frames = [] 
for i in range(5): 
    frame = np.full((4, 4), i) # 사진 한 장을 얻었다고 가정 
    frames.append(frame) # 리스트에 담아 두기 

video = np.stack(frames) # 마지막에 한 번 쌓기 
print(video.shape) # (5, 4, 4) 
print(video)
