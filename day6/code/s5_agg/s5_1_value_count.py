import pandas as pd 

label = pd.Series(
    ["person", "helmet", "car", "person", "forklift", "person",  "helmet", "car"]) 
print(label.value_counts()) # person 3, helmet 2, car 2, forklift 1 
print(label.value_counts(normalize=True)) # 비율로: person 0.375 ... 
