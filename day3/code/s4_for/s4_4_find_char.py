cnt = 0

target = input('원본 문자열')
find = input('찾는 문자')

for i in target:
    if  i == find:
        cnt += 1

print(f'{target}에서 {find} 개수: {cnt}개')