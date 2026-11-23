import pandas as pd 


df = pd.DataFrame({ 
    "time": pd.to_datetime([ 
    "2026-11-20 09:00:01", "2026-11-20 09:00:01", "2026-11-20 09:00:03", "2026-11-20 09:00:04", 
    "2026-11-20 09:00:06", "2026-11-20 09:00:07", "2026-11-20 09:00:09", "2026-11-20 09:00:10"]), 
    "label": ["person", "helmet", "car", "person", "forklift", "person", "helmet",  "car"], 
    "latency_ms": [32.5, 32.5, 41.2, 38.0, 29.8, 47.3, 30.1, 44.7], 
}) 


ts = df.set_index("time").sort_index() 

print(ts.resample("5s").size()) # 5 초마다 몇 개 찾았나 
# 09:00:00 4 ← 0~4 초 
# 09:00:05 3 ← 5~9 초 
# 09:00:10 1 ← 10~14 초 

print(ts["latency_ms"].resample("5s").agg(["mean", "max"]).round(1)) # 5 초마다 
