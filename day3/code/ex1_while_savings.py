# while문 예제: 목표 금액을 모을 때까지 매달 저축하기

goal = 100000      # 목표 금액
monthly = 15000    # 매달 저축하는 금액
savings = 0        # 현재 모은 금액
month = 0          # 지난 개월 수

# 모은 금액이 목표보다 적은 동안 계속 반복
while savings < goal:
    month += 1
    savings += monthly
    print(f"{month}개월차: {savings}원 저축")

print(f"목표 {goal}원 달성까지 {month}개월이 걸렸습니다!")
