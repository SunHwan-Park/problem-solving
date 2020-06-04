import sys
sys.stdin = open('input.txt')

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(cx, cy, cost):
    global min_cost
    if cost >= min_cost:
        return
    elif cx == N-1 and cy == N-1:
        min_cost = cost
    else:
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < N and 0 <= ny < N and V[nx][ny] == 0:
                V[nx][ny] = 1
                dfs(nx, ny, cost+M[nx][ny])
                V[nx][ny] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    M = [list(map(int, list(input()))) for _ in range(N)]
    V = [[0]*N for _ in range(N)]
    V[0][0] = 1
    min_cost = 500
    dfs(0, 0, 0)
    print('#{} {}'.format(tc, min_cost))