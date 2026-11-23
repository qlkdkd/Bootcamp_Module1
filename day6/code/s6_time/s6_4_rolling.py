import pandas as pd 
lat = pd.Series([32.5, 32.5, 41.2, 38.0, 29.8, 47.3, 30.1, 44.7]) 
ma3 = lat.rolling(3, min_periods=1).mean().round(2) # 최근 3 개의 평균 
print(pd.DataFrame({"원래 값": lat, "최근 3 개 평균": ma3, "앞 값과 차이": lat.diff()}))
