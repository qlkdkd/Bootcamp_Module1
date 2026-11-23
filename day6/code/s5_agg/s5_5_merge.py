import pandas as pd 

log = pd.DataFrame({ 
    "camera": ["cam1", "cam2", "cam1", "cam3"], 
    "label": ["person", "car", "helmet", "person"], 
})

cams = pd.DataFrame({ 
    "camera": ["cam1", "cam2"], 
    "location": ["입구", "작업장"], 
}) 

print('log')
print(log)
print('cams')
print(cams)


print('left join')
print(log.merge(cams, on="camera", how="left")) # 기록은 전부 남기고 위치를 붙임 (cam3 은 위치가 없어 NaN) 

print('inner join')
print(log.merge(cams, on="camera", how="inner")) # 양쪽에 모두 있는 것만 (cam3 줄이 빠짐) 
