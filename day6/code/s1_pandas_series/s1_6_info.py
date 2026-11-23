import pandas as pd 

df = pd.DataFrame({ 
 "camera":\
      ["cam1", "cam1", "cam2", "cam2", "cam1", "cam2"], 
 "label":\
      ["person", "helmet", "car", "Person", "person", "car"],
 "conf": \
    [0.91, 0.85, 0.77, 0.42, None, 0.95], 
}) 


print('---head---')
print(df.head(3)) # 앞 3 줄 보기 (뒤는 tail) 
print('---info---')
df.info() # 줄 수, 열별 종류, 빈 값이 아닌 값의 개수 (스스로 출력함) 

print('---describe---')
print(df.describe()) # 숫자 열의 개수·평균·최솟값·최댓값 등 요약 

print('---value_count---')
print(df["label"].value_counts()) # 값마다 몇 번 나오는지 (많은 순) 
