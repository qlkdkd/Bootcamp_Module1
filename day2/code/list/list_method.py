a = [1, 2, 3]
a.append(4)
print(a)

a = [1, 4, 3, 2]
a.sort()
print(a)

a = [1, 4, 3, 2]
a.sort(reverse=True)
print(a)

a = [1, 4, 2, 3]
a.reverse()
print(a)

a = [1, 2, 3]
print(a.index(3))
#rint(a.index(0)) # 에러!

b = [1, 1, 2]
print(b.index(1))