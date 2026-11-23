import pandas as pd 


df = pd.DataFrame({ 
    "camera": ["cam1", "cam1", "cam2", "cam2", "cam1", "cam2", "cam1", "cam2"],  
    "label": ["person", "helmet", "car", "person", "forklift", "person", "helmet", "car"], 
     "conf": [0.91, 0.85, 0.77, 0.42, 0.66, 0.88, 0.58, 0.95], 
}) 

print('sorted(conf descending)')
print(df.sort_values("conf", ascending=False));print() # 신뢰도 높은 순 

print('sorted(camera-ascending, cofn-descending)')
print(df.sort_values(
    ["camera", "conf"], ascending=[True, False]
    )
);print() # 카메라별로 묶고, 그 안에서 신뢰도 높은 순 

print('conf top3')
print(df.nlargest(3, "conf")); print() # 신뢰도 상위 3 개 


result = df[df["conf"] >= 0.8]\
    .sort_values("conf").reset_index(drop=True)

print('sorted conf if conf >= 0.8')
print(result) # 줄 이름표가 0, 1, 2, 3 으로 새로 붙음 
