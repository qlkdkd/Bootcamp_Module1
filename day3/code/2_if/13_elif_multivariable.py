a = 30
speed = 20
car_speed = 20


if a >= 130:
    print('보행 중')

    if speed >= 30:
        print('뛰는 중')
        
        if car_speed > speed:
            print('비상정지')

        else:
            print('서행 경고')

    else: print('걷는 중')

elif a >= 80:
    print('앉은 자세')

elif a >= 10:
    print('엎드려있음')

else:
    print('발견하지 못함')