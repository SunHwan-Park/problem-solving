import sys
sys.stdin = open('input.txt')

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def f(ci, cj, count):
    global N, result, dx, dy
    for k in range(4):
        ni = ci + dx[k]
        nj = cj + dy[k]
        if 0 <= ni < N and 0 <= nj < N and V[ni][nj] == 0:
            if M[ni][nj] == '0':
                V[ni][nj] = 1
                f(ni, nj, count+1)
                V[ni][nj] = 0
            elif M[ni][nj] == '3':
                result = count
                return
                
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    M = [list(input()) for _ in range(N)]
    si, sj = -1, -1
    for i in range(N):
        for j in range(N):
            if M[i][j] == '2':
                si, sj = i, j
                break
        if si >= 0:
            break
    V = [[0]*N for _ in range(N)]
    V[si][sj] = 1
    result = 0
    f(si, sj, 0)
    print('#{} {}'.format(tc, result))