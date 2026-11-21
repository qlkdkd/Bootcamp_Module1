strings = '''
ajskdvnqkengkoqnkdm,lavm,lcv a;mdnngflkent  [wpgvm;lads,. lgnkjfsz]
'''

def search_char(x: str):
    cnt = 0
    idxs = []
    for idx in range(len(strings)):
        if x == strings[idx]:
            cnt += 1
            idxs.append(idx)
            print(f'{idx+1}번째 글자에 {x}있음')
    return cnt, idxs

x = 'a'
cnt, idxs = search_char(x)
print(f'{x}는 {[i+1 for i in idxs]}번째 위치에 있고 총 {cnt}개만큼 있음')