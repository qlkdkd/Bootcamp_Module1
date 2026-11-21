import numpy as np 


# 열: 온도(℃), 습도(%), 거리(mm) 
sensor = np.array(
    [[22.1, 45.0, 1200], 
    [23.5, 50.2, 800], 
    [21.8, 48.7, 1500], 
    [24.0, 52.1, 950]]) 

mn = sensor.min(axis=0) # 열마다 최솟값 (3 개) 
mx = sensor.max(axis=0) # 열마다 최댓값 (3 개) 

norm = (sensor - mn) / (mx - mn) 

print(mn) # [ 21.8 45. 800. ]
print(mx) # [ 24. 52.1 1500. ] 
print(norm.round(2)) # 모든 값이 0~1 사이로 바뀜 
