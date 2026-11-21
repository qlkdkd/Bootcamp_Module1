cnt = 0

find_char = input('찾을 문자 입력: ')


for i in "hello":
    if i == find_char:
        cnt += 1

print(f'찾는 문자 {find_char}: {cnt}개')