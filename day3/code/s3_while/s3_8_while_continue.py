y = 0


while True:
    y += 1

    if y % 2 == 0:
        print(f'y값: {y:2d}')

    else:
        continue # y가 홀수면 넘어감

    if y == 10:
        break