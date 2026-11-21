f = open('./새파일.txt', 'r')
lines = f.readlines()

for line in lines:
    line = line.strip() # 줄 끝의 줄바꿈 문자 제거
    print(line)

f.close()