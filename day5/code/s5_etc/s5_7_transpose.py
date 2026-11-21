import numpy as np 
x = np.array([
    [1, 2, 3], 
    [4, 5, 6]]) # 2 줄 3 칸 

print(x.T) # 3 줄 2 칸 
# [[1 4] 
# [2 5] 
# [3 6]] 

print(x.reshape(3, 2)) # reshape 와 비교 
# [[1 2] 
# [3 4] 
# [5 6]] 
