for _ in range(4):
    data = list(map(int, input().split()))
    x_overlap = len(set(range(data[0], data[2]+1)) & set(range(data[4], data[6]+1)))
    y_overlap = len(set(range(data[1], data[3]+1)) & set(range(data[5], data[7]+1)))
    if x_overlap == 0 or y_overlap == 0:
        print('d')
    elif x_overlap == 1 and y_overlap == 1:
        print('c')
    elif x_overlap == 1 or y_overlap == 1:
        print('b')
    else:
        print('a')