import pandas as pd 

df = pd.DataFrame({ 
 "camera": ["cam1", "cam1", "cam2", "cam2", "cam1", "cam2", "cam1", "cam2"],  
 "label": ["person", "helmet", "car", "person", "forklift", "person", "helmet",  "car"], 
 "conf": [0.91, 0.85, 0.77, 0.42, 0.66, 0.88, 0.58, 0.95], 
})

print('전체 데이터')
print(df)

print('---loc[0](행 이름: 0)---')
print(df.loc[0]) # 이름표가 0 인 줄 

print('---loc[0:2, [label, conf]](행 이름이 0~2, 열 이름이 label, conf)---')
print(df.loc[0:2, ["label", "conf"]]) # 이름표 0~2 (2 포함 → 3 줄), 두 열 

print('---loc[3, conf]행 이름이 3, 열 이름이 conf---')
print(df.loc[3, "conf"]) # 0.42 ← 이름표 3 번 줄의 conf 값 하나 


print('---iloc[0:2, 1:3] 0~2번째 행, 1~3번째 열---')
print(df.iloc[0:2, 1:3]) # 위에서 0~1 번째 줄, 1~2 번째 열 (2 줄) 

print('---loc[-1](마자막 행)---')
print(df.iloc[-1]) # 맨 끝 줄 


top = df.sort_values("conf", ascending=False) # 신뢰도 높은 순으로 정렬 print(top) 
print(top)

print('---conf 기준으로 역정렬한 데이터에서 행 이름이 0, 열 이름이 label인 데이터---')
print(top.loc[0, "label"]) # person ← 이름표가 0 인 줄 (원래 맨 윗줄) — 어디로 옮겨졌든 찾아옴 

print('---conf 기준으로 역정렬한 데이터에서 0행에 있는 label열에 있는 데이터---')
print(top.iloc[0]["label"]) # car ← 지금 맨 위에 있는 줄 (신뢰도 1 등 0.95)
