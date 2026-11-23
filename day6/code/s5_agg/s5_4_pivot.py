import pandas as pd 
df = pd.DataFrame({ 
    "camera": ["cam1", "cam1", "cam2", "cam2", "cam1", "cam2", "cam1", "cam2"],  
    "label": ["person", "helmet", "car", "person", "forklift", "person", "helmet",  "car"], 
    "conf": [0.91, 0.85, 0.77, 0.42, 0.66, 0.88, 0.58, 0.95], 
}) 

print(pd.pivot_table(
    df, 
    index="label", 
    columns="camera", 
    values="conf",  
    aggfunc="mean")
) 

# 줄: 종류, 열: 카메라, 칸: 평균 conf (해당 조합이 없으면 NaN) 
print(pd.crosstab(
    df["label"], df["camera"], margins=True
    )
) # 개수 표 + 합계(All)  줄·칸 
