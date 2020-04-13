import sys
sys.stdin = open('input.txt')

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs():
    while queue:
        ci, cj = queue.pop(0)
        for k in range(4):
            ni = ci + dx[k]
            nj = cj + dy[k]
            if 0 <= ni < N and 0 <= nj < N and V[ni][nj] == 0:
                if M[ni][nj] == '0':
                    queue.append((ni, nj))
                    V[ni][nj] = V[ci][cj] + 1
                elif M[ni][nj] == '3':
                    return V[ci][cj] - 1
    return 0
                
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    M = [list(input()) for _ in range(N)]
    V = [[0]*N for _ in range(N)]
    si, sj = -1, -1
    for i in range(N):
        for j in range(N):
            if M[i][j] == '2':
                si, sj = i, j
                break
        if si >= 0:
            break
    
    queue = [(si, sj)]
    V[si][sj] = 1
    print('#{} {}'.format(tc, bfs()))