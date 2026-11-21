def div(a, b):
    if b == 0:
        print('Can\'t divide to zero')
        return
    return a // b

print(div(3, 2))
print(div(3, 0))