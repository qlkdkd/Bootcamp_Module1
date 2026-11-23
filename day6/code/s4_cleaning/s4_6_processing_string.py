import pandas as pd 

df = pd.DataFrame({ 
    "label": ["person", "Person", " car", "helmet", "PERSON "],
    "resolution": ["640x480", "1280x720", "640x480", "1920x1080", "640x480"], 
}) 

print('---before str processing---')
print(df["label"].unique()) # 같은 person 이 여러 가지로 적혀 있다 
print(df["label"].value_counts()) 


# str 작업 처리
df["label"] = df["label"].str.lower().str.strip() # 모두 소문자로, 앞뒤 공백 지우기 

print('---after str processing---')
print(df["label"].value_counts()) # person 3, car 1, helmet 1 
print(df["label"].str.contains("er")) # "er"이 들어 있는지 (True/False) 

print(df["label"].str.len()) # 글자 수 
wh = df["resolution"].str.split("x", expand=True).astype(int) # "x"를 기준으로 잘라 두 열로 
wh.columns = ["width", "height"] 
print(wh) 
