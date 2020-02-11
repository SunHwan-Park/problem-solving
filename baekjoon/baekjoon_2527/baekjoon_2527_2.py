for _ in range(4):
    data = list(map(int, input().split()))
    rec1 = data[:4]
    rec2 = data[4:]
    matrix = [[0 for _ in range(max(data)+1)] for _ in range(max(data)+1)]

    if rec1[0] < rec2[0]:
        rec1[0] += 1
        rec1[2] += 1
    else:
        rec2[0] += 1
        rec2[2] += 1
    if rec1[1] < rec2[1]:
        rec1[1] += 1
        rec1[3] += 1
    else:
        rec2[1] += 1
        rec2[3] += 1

    for i in range(rec1[0], rec1[2]):
        for j in range(rec1[1], rec1[3]):
            matrix[i][j] += 1
    for i in range(rec2[0], rec2[2]):
        for j in range(rec2[1], rec2[3]):
            matrix[i][j] += 1

    count_row = 0
    count_col = 0
    for i in range(max(data)):
        if 2 in matrix[i]:
            count_row += 1
        temp = []
        for j in range(max(data)):
            temp.append(matrix[j][i])
        if 2 in temp:
            count_col += 1

    if count_row == 0 and count_col == 0:
        print('d')
    elif count_row == 1 and count_col == 1:
        print('c')
    elif count_row == 1 or count_col == 1:
        print('b')
    else:
        print('a')