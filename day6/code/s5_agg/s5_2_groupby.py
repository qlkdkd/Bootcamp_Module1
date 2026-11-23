import pandas as pd 


df = pd.DataFrame({ 
    "camera": ["cam1", "cam1", "cam2", "cam2", "cam1", "cam2", "cam1", "cam2"],  
    "label": ["person", "helmet", "car", "person", "forklift", "person", "helmet",  "car"], 
    "conf": [0.91, 0.85, 0.77, 0.42, 0.66, 0.88, 0.58, 0.95], 
}) 


print('conf를 label별로 나눠서 평균내기')
print(df.groupby("label")["conf"].mean().round(3)) # label 별로 나눠서 conf 평균 # label 
print()
# car 0.860 
# forklift 0.660 
# helmet 0.715 
# person 0.737 
print('conf를 label로 분류해서 개수, 평균, 최댓값 구하기')
print(df.groupby("label")["conf"].agg(["count", "mean", "max"]).round(3)) # 계산 여러 개를 한꺼번에 
print()

print('camera별로 나누고, label로 또 나눠서 개수 구하기')
print(df.groupby(["camera", "label"]).size()) # 카메라별 ×  종류별로 두 번 나눠서 개수 
