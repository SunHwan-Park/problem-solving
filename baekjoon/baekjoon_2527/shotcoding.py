for _ in range(4):
    d = list(map(int,input().split()))
    x = len(set(range(d[0], d[2]+1))&set(range(d[4], d[6]+1)))
    y = len(set(range(d[1], d[3]+1))&set(range(d[5], d[7]+1)))
    if 0 in [x,y]:
        a='d'
    elif (x,y) == (1,1):
        a='c'
    elif 1 in [x,y]:
        a='b'
    else:
        a='a'
    print(a)