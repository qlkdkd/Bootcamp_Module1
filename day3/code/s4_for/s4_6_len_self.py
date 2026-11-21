def length(l: list):
    cnt = 0
    for i in l:
        if i:
            cnt += 1

    return cnt

l = input()
print(length(l))