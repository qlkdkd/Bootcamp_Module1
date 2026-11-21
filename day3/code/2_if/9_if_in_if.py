a = 100

if a>50:
    print('50 이상')
    if a>60:
        print('60 이상')


a = 30

if a > 50:
    print(50)
    if a > 60:
        print(60)
        if a > 70:
            print(70)

else:
    print('else')


a = 60

if a > 50:
    print(50)
    if a > 60:
        print(60)
        if a > 70:
            print(70)
        else:
            print('under 70')
    else: print('under 60')
else:
    print('else')