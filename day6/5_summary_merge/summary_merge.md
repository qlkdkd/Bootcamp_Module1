# 묶어서 요약하기와 표 합치기

## value_counts: 개수 세기
- `df.value_counts()`: 값의 개수
    - 변수가 범주형일때 자주 사용

```py
import pandas as pd 

label = pd.Series(
    ["person", "helmet", "car", "person", "forklift", "person",  "helmet", "car"]) 
print(label.value_counts()) # person 3, helmet 2, car 2, forklift 1 
print(label.value_counts(normalize=True)) # 비율로: person 0.375 ... 

```
```
person      3
helmet      2
car         2
forklift    1
Name: count, dtype: int64
person      0.375
helmet      0.250
car         0.250
forklift    0.125
Name: proportion, dtype: float64
```
- `df.groupby(기준_열)[나눌_열].계산_메서드`: 나눠서 계산하고 모으기

```py
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

```
```
conf를 label별로 나눠서 평균내기
label
car         0.860
forklift    0.660
helmet      0.715
person      0.737
Name: conf, dtype: float64

conf를 label로 분류해서 개수, 평균, 최댓값 구하기
          count   mean   max
label                       
car           2  0.860  0.95
forklift      1  0.660  0.66
helmet        2  0.715  0.85
person        3  0.737  0.91

camera별로 나누고, label로 또 나눠서 개수 구하기
camera  label   
cam1    forklift    1
        helmet      2
        person      1
cam2    car         2
        person      2
dtype: int64
```

## agg: 요약표 한 번에
- `agg([여러가지 메서드])`: 데이터프레임의 메서드를 담은 리스트를 매개변수로 전달. 메서드의 결과들이 담긴 데이터프레임 반환
```py
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
```
```
          n  conf_mean  lat_max
label                          
car       2       0.86     44.7
forklift  1       0.66     29.8
helmet    2       0.72     32.5
person    3       0.74     47.3
```
- n, conf_mean, lat_max: 파생 변수
    - 파생 변수: 기존 변수들을 계산하여 나온 새로운 변수

## 피벗
- 피벗: 표를 가로로 펼치기
```py
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
```
```
camera     cam1  cam2
label                
car         NaN  0.86
forklift  0.660   NaN
helmet    0.715   NaN
person    0.910  0.65
camera    cam1  cam2  All
label                    
car          0     2    2
forklift     1     0    1
helmet       2     0    2
person       1     2    3
All          4     4    8
```

## merge
- 사원 명단(사번, 이름)과 근태표(사번, 출근 시각)가 따로 있을 때, 사번을 보고 짝을 맞춰 "사번,  이름, 출근 시각" 표를 만드는 것이 merge 다. 
- 엑셀의 VLOOKUP 과 비슷하다. 
- 탐지 기록에는 카메라 이름만 있고, 카메라가 어디 설치됐는지는 별도 표에 있다. 둘 다 가진 camera 열로 짝을 맞춘다. 

```py
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

```
```
log
  camera   label
0   cam1  person
1   cam2     car
2   cam1  helmet
3   cam3  person
cams
  camera location
0   cam1       입구
1   cam2      작업장
left join
  camera   label location
0   cam1  person       입구
1   cam2     car      작업장
2   cam1  helmet       입구
3   cam3  person      NaN
inner join
  camera   label location
0   cam1  person       입구
1   cam2     car      작업장
2   cam1  helmet       입구
```

## concat
- 옆으로 붙이기