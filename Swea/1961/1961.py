test_size = int(input())
for t in range(test_size):
    n = int(input())
    matrix = []
    for _ in range(n):
        matrix.append(input().split())
    
    matrix_90 = [[0]*n for _ in range(n)]
    matrix_180 = [[0]*n for _ in range(n)]
    matrix_270 = [[0]*n for _ in range(n)]
        
    for i in range(n):
        for j in range(n):
            matrix_90[j][n-1-i] = matrix[i][j]
            matrix_180[n-1-i][n-1-j] = matrix[i][j]
            matrix_270[n-1-j][i] = matrix[i][j]
    
    print('#{}'.format(t+1))
    for i in range(n):
        print(''.join(matrix_90[i]), ''.join(matrix_180[i]), ''.join(matrix_270[i]))