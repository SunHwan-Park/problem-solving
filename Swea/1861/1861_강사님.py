import sys
sys.stdin = open('n1000.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    M = [list(map(int, input().split())) for _ in range(N)]
    V = [0] * (N * N + 1)

    for i in range(N):
        for j in range(N):
            if i != N-1 and M[i+1][j] == M[i][j] + 1:
                V[M[i][j]] = 1
            elif i != 0 and M[i-1][j] == M[i][j] + 1:
                V[M[i][j]] = 1
            elif j != N-1 and M[i][j+1] == M[i][j] + 1:
                V[M[i][j]] = 1
            elif j != 0 and M[i][j-1] == M[i][j] + 1:
                V[M[i][j]] = 1
    
    length = 0
    idx = 0
    temp = 0
    for i in range(N * N + 1):
        if V[i] == 1:
            temp += 1
        else:
            if temp > length:
                length = temp
                idx = i - length
            temp = 0
    print('#{} {} {}'.format(tc, idx, length+1))