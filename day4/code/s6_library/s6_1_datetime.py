import datetime

day1 = datetime.date(2021, 12, 13)
day2 = datetime.date(2023, 4, 5)

print(day1, day2)

# datetime.date의 type
print(type(day1))


diff = day2 - day1

# 두 날짜의 차이의 일수
print(diff.days)
