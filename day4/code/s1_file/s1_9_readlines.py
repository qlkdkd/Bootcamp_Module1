f = open('./새파일.txt', 'r')
lines = f.readlines()

for line in lines:
    print(line)

print(lines)
f.close()