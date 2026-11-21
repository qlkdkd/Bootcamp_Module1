result1 = [x * y  for x in range(1, 10) for y in range(1, 5)]
print(result1)

# 얘랑 같음
result2 = []
for x in range(1, 10):
    for y in range(1, 5):
        result2.append(x * y)

print(result2)

print(result1 == result2)