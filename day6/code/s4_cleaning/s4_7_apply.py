import numpy as np 
import pandas as pd 


conf = pd.Series([0.91, 0.42, np.nan, 0.66, 0.85]) 

def grade(c): 
    if pd.isna(c): # 빈 칸이면 
        return "unknown" 
    if c >= 0.8: 
        return "high" 
    if c >= 0.5: 
        return "mid" 
    return "low" 


print(conf.apply(grade).tolist()) # ['high', 'low', 'unknown', 'mid', 'high'] 
