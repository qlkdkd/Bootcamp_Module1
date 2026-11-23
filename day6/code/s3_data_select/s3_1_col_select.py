import pandas as pd 

df = pd.DataFrame({ 
 "camera": ["cam1", "cam1", "cam2", "cam2", "cam1", "cam2", "cam1", "cam2"],  "label": ["person", "helmet", "car", "person", "forklift", "person", "helmet",  "car"], 
 "conf": [0.91, 0.85, 0.77, 0.42, 0.66, 0.88, 0.58, 0.95], 
}) 

print(df["label"]) # 열 하나 → Series 
print(df[["label", "conf"]]) # 열 여러 개 → 표 (대괄호가 두 겹) 