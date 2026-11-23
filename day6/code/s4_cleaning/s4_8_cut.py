import numpy as np 
import pandas as pd 

conf = pd.Series([0.91, 0.42, np.nan, 0.66, 0.85]) 
g = pd.cut(
    conf, 
    bins=[0, 0.5, 0.8, 1.0], 
    labels=["low", "mid", "high"], 
    right=False
)
 
print(g.tolist()) # ['high', 'low', nan, 'mid', 'high'] 
# 0 이상 0.5 미만 → low, 0.5 이상 0.8 미만 → mid, 0.8 이상 → high 
