while True:
    cnt = 0
    target = input('원본 문자열: ')
    find = input('찾을 문자: ')

    for i in target:
        if i == find:
            cnt += 1

    if cnt == 0:
        print('찾는 문자가 없음')
        break

    else:
        print('찾은 문자 개수:', cnt)
        break
print('while 밖')