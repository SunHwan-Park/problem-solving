def checknode(i, j):
    if i == N - 1:
        if row[i] == 0 and col[j] == 0 and right[i + j] == 0 and left[i + N - 1 - j] == 0:
            matrix[i][j] = 1
            row[i] = 1
            col[j] = 1
            right[i + j] = 1
            left[i + N - 1 - j] = 1
            result.append(matrix)
    else:
        if row[i] == 0 and col[j] == 0 and right[i + j] == 0 and left[i + N - 1 - j] == 0:
            matrix[i][j] = 1
            row[i] = 1
            col[j] = 1
            right[i + j] = 1
            left[i + N - 1 - j] = 1
            for k in range(N):
                checknode(i+1, k)
            else:
                matrix[i][j] = 0
                row[i] = 0
                col[j] = 0
                right[i + j] = 0
                left[i + N - 1 - j] = 0




T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [[0 for _ in range(N)] for _ in range(N)]
    row = [0]*N
    col = [0]*N
    right = [0]*(2*N-1)
    left = [0]*(2*N-1)
    result = []

    for j in range(N):
        checknode(0, j)

    print(result)