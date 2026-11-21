import numpy as np 


# x1 y1 x2 y2 
boxes = np.array([
    [ 50, 40, 150, 200], 
    [200, 100, 260, 160], 
    [ 10, 10, 30, 50]], 
    dtype=np.float32) # 상자 3 개 


w = boxes[:, 2] - boxes[:, 0] # 너비 = x2 - x1 (모든 상자 한 번에) 
h = boxes[:, 3] - boxes[:, 1] # 높이 = y2 - y1 
cx = (boxes[:, 0] + boxes[:, 2]) / 2 # 가운데 x 
cy = (boxes[:, 1] + boxes[:, 3]) / 2 # 가운데 y 
area = w * h # 넓이 

print("너비:", w) # [100. 60. 20.] 
print("높이:", h) # [160. 60. 40.] 
print("중심:", np.stack([cx, cy], axis=1)) 
print("넓이:", area) # [16000. 3600. 800.] 
print()


# 작게 줄여서 찾은 결과를 원래 크기로 되돌리기 (320×240 → 1280×960, 가로·세로 4 배) 
boxes_big = boxes * 4 
print(boxes_big[0]) # [200. 160. 600. 800.] 
# 너무 작은 상자는 버리기 
keep = area >= 1000 
print(boxes[keep]) # 앞의 두 상자만 남음 
