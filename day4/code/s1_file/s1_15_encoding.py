with open('hangul.txt', 'w', encoding='utf-8') as f:
    f.write('ㅁㄴㅇㄿㅊ미ㅏ')

with open('hangul.txt', 'r') as f:
    data = f.read()

print(data)