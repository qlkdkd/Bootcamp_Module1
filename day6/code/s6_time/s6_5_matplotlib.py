import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 


plt.rcParams["font.family"] = "Malgun Gothic" # 맑은 고딕 (macOS 는 "AppleGothic") 
plt.rcParams["axes.unicode_minus"] = False # 마이너스(-) 기호 깨짐 방지 


# 연습용 기록 300 개 만들기: 1 초 간격, 처리 시간은 35ms 근처에서 흔들림 
rng = np.random.default_rng(0) 


df = pd.DataFrame({ 
    "time": pd.date_range("2026-11-20 09:00:00", periods=300, freq="1s"),  
    "camera": rng.choice(["cam1", "cam2"], 300), 
    "label": rng.choice(["person", "car", "helmet", "forklift"], 300, p=[0.4, 0.2,  0.25, 0.15]), 
    "conf": rng.uniform(0.3, 0.99, 300).round(3), 
    "latency_ms": rng.normal(35, 6, 300).round(1), 
}) 


ts = df.set_index("time") 
print(df.head()) 


per_min = ts.resample("1min").size() # 1 분마다 개수 
lat_ma = ts["latency_ms"].rolling(20, min_periods=1).mean() # 최근 20 개 평균 
print(per_min) 


fig, axes = plt.subplots(2, 2, figsize=(12, 7)) # 2×2 칸에 그래프 4 개 
per_min.plot.bar(ax=axes[0, 0], title="분당 탐지 개수") 


ts["latency_ms"].plot(ax=axes[0, 1], alpha=0.3, label="원래 값") # 연하게 
lat_ma.plot(ax=axes[0, 1], label="최근 20 개 평균", title="처리 시간(ms)") 
axes[0, 1].legend() # 범례 표시 
df["label"].value_counts().plot.bar(ax=axes[1, 0], title="종류별 탐지 개수") 
df["conf"].plot.hist(bins=20, ax=axes[1, 1], title="신뢰도 분포") 
plt.tight_layout() # 그래프끼리 겹치지 않게 간격 조절 

plt.savefig("./day6/code/s6_time/chart.png", dpi=150) # 그림 파일로 저장 (show 보다 먼저) 
plt.show() 

print("chart.png 저장 완료")
