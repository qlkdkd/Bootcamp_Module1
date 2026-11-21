def mixed_function(name, *args, **kwargs):
    print(f'이름: {name}')
    print(f'추가 인수들: {args}')
    print(f'키워드 인수들: {kwargs}')


mixed_function('홍길동',
               1, 2, 3,
               age=25, city='서울')