import pandas as pd 

df = pd.DataFrame({ 
    "label": ["person", "helmet", "car", "person", "forklift", "person", "helmet",  "car"], 
    "conf": [0.91, 0.85, 0.77, 0.42, 0.66, 0.88, 0.58, 0.95], 
    "latency_ms": [32.5, 32.5, 41.2, 38.0, 29.8, 47.3, 30.1, 44.7], })

# label로 묶어서, 개수/신뢰도/최댓값 반환
summary = df.groupby("label").agg(
    n=("conf", "size"), # 개수 
    conf_mean=("conf", "mean"), # 평균 신뢰도 
    lat_max=("latency_ms", "max"), # 가장 오래 걸린 처리 시간 
).round(2) 

print(summary) 