print('기존 리스트')
a = [1, 2, 3, 4]
result = []

for num in a:
    result.append(num*3)

print(result)


print('리스트 컴프리헨션')
a = [1, 2, 3, 4]
result = [num*3 for num in a]
print(result)