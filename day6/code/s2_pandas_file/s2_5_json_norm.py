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
