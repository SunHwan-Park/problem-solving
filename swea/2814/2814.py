import sys
sys.stdin = open('input.txt')

def dfs(node, length):
    global max_length
    for i in range(1, N+1):
        if matrix[node][i] == 1 and V[i] == 0:
            V[i] = 1
            dfs(i, length+1)
            V[i] = 0
    else:
        if length > max_length:
            max_length = length
        return

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [[0]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        x, y = map(int, input().split())
        matrix[x][y] = 1
        matrix[y][x] = 1
    V = [1]+[0]*N
    max_length = 1
    for i in range(1, N+1):
        V[i] = 1
        dfs(i, 1)
        V[i] = 0
    print('#{} {}'.format(tc, max_length))