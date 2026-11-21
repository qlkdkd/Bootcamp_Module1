import numpy as np 

conf = np.array([0.91, 0.32, 0.77, 0.15, 0.58]) 

print(conf[
    (conf > 0.3) & (conf < 0.8)
    ]) # [0.32 0.77 0.58] 0.3 보다 크고 그리고 0.8 보다 작은 

print(conf[
    (conf < 0.2) | (conf > 0.9)
    ]) # [0.91 0.15] 0.2 보다 작거나 또는 0.9 보다 큰 

print(conf[
    ~(conf > 0.5)
    ]) # [0.32 0.15] 0.5 보다 크지 않은
