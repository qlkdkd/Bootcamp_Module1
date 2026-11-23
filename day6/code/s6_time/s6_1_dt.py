import pandas as pd 


t = pd.Series(pd.to_datetime(
    ["2026-11-20 09:00:01", "2026-11-20 09:05:30", "2026-11-20 10:12:45"]
)) 


print(t.dt.hour.tolist()) # [9, 9, 10] 몇 시 
print(t.dt.minute.tolist()) # [0, 5, 12] 몇 분 
print(t.dt.day_name().tolist()) # ['Friday', 'Friday', 'Friday'] 요일 
print(t.dt.strftime("%H:%M").tolist()) # ['09:00', '09:05', '10:12'] 원하는 모양의 글자로 
print(t.max() - t.min()) # 0 days 01:12:44 시간 차이 
print((t + pd.Timedelta(hours=9)).tolist()[0]) # 2026-11-20 18:00:01 9 시간 더하기
