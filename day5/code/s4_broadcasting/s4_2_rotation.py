import numpy as np 

R = np.array([
    [0, -1], 
    [1, 0]]) # 90 도 회전용 숫자표 

t = np.array([0.5, 0.0]) # 카메라가 로봇에서 떨어진 거리 (m) 

obj_cam = np.array([
    [0.10, 0.05], 
    [0.30, -0.02]]) # 카메라가 본 물체 2 개의 위치 (m) 


obj_robot = obj_cam @ R.T + t # ① 돌리고(@) ② 옮기기(+) 

print(obj_robot) 
# [[0.45 0.1 ] 
# [0.52 0.3 ]] ← 로봇 기준 위치 