# 파일로 읽고 쓰기
- 데이터는 대부분 파일로 들어오고 나감
- `pd.read_` 형식을 읽고, `df_to`로 저장
- CSV 는 엑셀로도 열리고 사람이 읽기 쉽다. JSON 은 프로그램끼리 데이터를 주고받을 때(웹, 장치 간 통신, 설정 파일) 많이 쓴다. 

## CSV 파일 읽기
- csv 읽기: `pd.read_csv(가져올_파일_경로)`
    ```py
    import pandas as pd

    root = r'C:\Users\Admin\Desktop\workspace\python_basic\day6\code\s2_pandas_file\vision_inspection_log.csv'
    df = pd.read_csv(root)

    print(df.head())
    print(df.info())
    print(df.describe())
    ```
    ```
                timestamp line_id camera_id part_id part_type  width_mm  height_mm  brightness defect_type  confidence  inference_ms result
    0  2026-11-23 09:00:01      L1     CAM01   P0001      bolt     12.02      40.11       128.0        none        0.98          23.4   PASS
    1  2026-11-23 09:00:03      L1     CAM01   P0002      bolt     11.97      39.95       131.0        none        0.97          22.8   PASS
    2  2026-11-23 09:00:05      L1     CAM01   P0003      bolt     12.10      40.30       126.0     scratch        0.88          24.1   FAIL
    3  2026-11-23 09:00:07      L1     CAM01   P0004       nut     10.01       8.02       135.0        none        0.99          21.9   PASS
    4  2026-11-23 09:00:09      L1     CAM01   P0005       nut      9.98       7.97         NaN        none        0.96          22.3   PASS
    <class 'pandas.DataFrame'>
    RangeIndex: 30 entries, 0 to 29
    Data columns (total 12 columns):
    #   Column        Non-Null Count  Dtype  
    ---  ------        --------------  -----  
    0   timestamp     30 non-null     str    
    1   line_id       30 non-null     str    
    2   camera_id     30 non-null     str    
    3   part_id       30 non-null     str    
    4   part_type     30 non-null     str    
    5   width_mm      30 non-null     float64
    6   height_mm     29 non-null     float64
    7   brightness    28 non-null     float64
    8   defect_type   30 non-null     str    
    9   confidence    29 non-null     float64
    10  inference_ms  30 non-null     float64
    11  result        30 non-null     str    
    dtypes: float64(5), str(7)
    memory usage: 2.9 KB
    None
            width_mm  height_mm  brightness  confidence  inference_ms
    count  30.000000  29.000000   28.000000   29.000000     30.000000
    mean   13.571000  19.641724  125.607143    0.914138     27.443333
    std     4.066046  17.645144    7.875604    0.085169      4.268140
    min     9.970000   1.980000  115.000000    0.690000     21.900000
    25%    10.110000   2.050000  119.000000    0.920000     23.025000
    50%    12.005000   8.020000  124.000000    0.950000     28.050000
    75%    18.032500  40.020000  131.500000    0.960000     30.775000
    max    20.400000  40.550000  140.000000    0.990000     34.700000
    ```

- 파일 저장: `df.to_csv('저장할 경로', index=False, encoding='utf-8')`
    - 저장할 경로에 인덱스는 생략해서, 인코딩은 utf-8로 저장한다는 의미


    ```py
    import os 
    import pandas as pd 

    root = r'C:\Users\Admin\Desktop\workspace\python_basic\day6\code\s2_pandas_file'

    os.makedirs(root + r"\data", exist_ok=True) # data 폴더가 없으면 만들기 

    df = pd.DataFrame({
    "time": ["2026-11-20 09:00:01", "2026-11-20 09:00:03", "2026-11-20 09:00:04"],  
    "camera": ["cam1", "cam2", "cam2"], 
    "label": ["person", "car", "person"], 
    "conf": [0.91, 0.77, 0.42], 
    }) 


    new_root = root + r'\data\sample.csv'
    df.to_csv(new_root, index=False, encoding="utf-8") # 저장 


    with open(new_root, encoding="utf-8") as f: # 파일 안이 어떻게 생겼는지 직접 보기 
        print(f.read()) 
    # time,camera,label,conf 
    # 2026-11-20 09:00:01,cam1,person,0.91 
    # ... 
    loaded = pd.read_csv(new_root, encoding="utf-8") # 다시 읽기 print(loaded) 
    print(loaded.dtypes) # time 이 글자(str)로 읽혔다 
    ```
    ```
    time,camera,label,conf
    2026-11-20 09:00:01,cam1,person,0.91
    2026-11-20 09:00:03,cam2,car,0.77
    2026-11-20 09:00:04,cam2,person,0.42

    time          str
    camera        str
    label         str
    conf      float64
    dtype: object
    ```

## csv 저장할 때 알아둘 것
- index=False: 줄 이름 표를 파일에 같이 저장 안함
    - 빼먹으면 다시 읽을 때 Unnamed: 0 이라는 처음 보는 열 생김
- utf-8-sig: 엑셀은 이 표식이 있어야 한글 utf-8 csv를 제대로 얻음

```py
import os 
import pandas as pd 

root = r'C:\Users\Admin\Desktop\workspace\python_basic\day6\code\s2_pandas_file\data'

os.makedirs(root, exist_ok=True) 

df = pd.DataFrame(
    {"label": ["사람", "차량"], 
     "conf": [0.91, 0.77]}) 

df.to_csv(
    root + r"\with_index.csv", 
    encoding="utf-8") # index=False 를 빼먹으면


print(pd.read_csv(
    root + r"\with_index.csv", encoding="utf-8")
) 


# Unnamed: 0 label conf ← 줄 이름표가 이상한 열로 따라 들어옴 
df.to_csv(
    root + r"/for_excel.csv", 
    index=False, 
    encoding="utf-8-sig"
) # 엑셀에서 열 한글 CSV 
print("저장 완료") 
```

## JSON 읽고 쓰기
- `df.to_json(경로, orient=True, force_ascii=False)`
    - 데이터프레임을 json 파일로 저장
    - orient=True: 한 줄을 {} 하나로 만들어라
    - force_ascii=False: 아스키 코드 지정 x
        - 얘 빼먹으면 한글이 사람이 읽을 수 없는 유니코드로 바뀌어버림
```py
import os 
import pandas as pd 

root = r'C:\Users\Admin\Desktop\workspace\python_basic\day6\code\s2_pandas_file\data'
os.makedirs(root, exist_ok=True) 

cams = pd.DataFrame({ 
    "camera": ["cam1", "cam2"], 
    "location": ["입구", "작업장"], 
    "resolution": ["640x480", "1280x720"],
}) 

cams.to_json(
    root + r"\cameras.json", 
    orient="records", 
    force_ascii=False, 
    indent=2
)

with open(root + r"\cameras.json", encoding="utf-8") as f: 
    print(f.read()) 
# [ 
# { 
# "camera":"cam1", 
# "location":"입구", 
# ... 
print(pd.read_json(root + r'\cameras.json')) 
```
```
[
  {
    "camera":"cam1",
    "location":"입구",
    "resolution":"640x480"
  },
  {
    "camera":"cam2",
    "location":"작업장",
    "resolution":"1280x720"
  }
]
  camera location resolution
0   cam1       입구    640x480
1   cam2      작업장   1280x720
```

### json 평탄화
```py
import pandas as pd 


response = [ 
 {
    "frame": 1, 
    "label": "person", 
    "conf": 0.91, 
    "box": {"x1": 10, "y1": 20, "x2":  60, "y2": 120}
  }, 

 {
    "frame": 1, 
    "label": "car", 
    "conf": 0.77, 
    "box": {"x1": 200, "y1": 50, "x2":  330, "y2": 140}
  }, 
] 


# 평평한 표로 만들어주기
flat = pd.json_normalize(response) 
print(flat.columns.tolist()) 
# ['frame', 'label', 'conf', 'box.x1', 'box.y1', 'box.x2', 'box.y2'] ← box 안의 값이 각각 열이 됨 
print(flat) 
```
```
['frame', 'label', 'conf', 'box.x1', 'box.y1', 'box.x2', 'box.y2']
   frame   label  conf  box.x1  box.y1  box.x2  box.y2
0      1  person  0.91      10      20      60     120
1      1     car  0.77     200      50     330     140
```