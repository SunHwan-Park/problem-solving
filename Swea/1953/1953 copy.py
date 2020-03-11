import sys
sys.stdin = open('input.txt')

def dfs(N, M, i, j, L):
    if L == 0:
        return
    else:
        psb_route.append((i, j))
        if matrix[i][j] == 1:
            if i != N-1 and matrix[i+1][j] in [1, 2, 4, 7] and psb_route.count((i+1, j)) < 1000:
                dfs(N, M, i+1, j, L-1)
            if i != 0 and matrix[i-1][j]   in [1, 2, 5, 6] and psb_route.count((i-1, j)) < 1000:
                dfs(N, M, i-1, j, L-1)
            if j != M-1 and matrix[i][j+1] in [1, 3, 6, 7] and psb_route.count((i, j+1)) < 1000:
                dfs(N, M, i, j+1, L-1)
            if j != 0 and matrix[i][j-1] in [1, 3, 4, 5] and psb_route.count((i, j-1)) < 1000:
                dfs(N, M, i, j-1, L-1)
        elif matrix[i][j] == 2:
            if i != N-1 and matrix[i+1][j] in [1, 2, 4, 7] and psb_route.count((i+1, j)) < 1000:
                dfs(N, M, i+1, j, L-1)
            if i != 0 and matrix[i-1][j] in [1, 2, 5, 6] and psb_route.count((i-1, j)) < 1000:
                dfs(N, M, i-1, j, L-1)
        elif matrix[i][j] == 3:
            if j != M-1 and matrix[i][j+1] in [1, 3, 6, 7] and psb_route.count((i, j+1)) < 1000:
                dfs(N, M, i, j+1, L-1)
            if j != 0 and matrix[i][j-1] in [1, 3, 4, 5] and psb_route.count((i, j-1)) < 1000:
                dfs(N, M, i, j-1, L-1)
        elif matrix[i][j] == 4:
            if i != 0 and matrix[i-1][j] in [1, 2, 5, 6] and psb_route.count((i-1, j)) < 1000:
                dfs(N, M, i-1, j, L-1)
            if j != M-1 and matrix[i][j+1] in [1, 3, 6, 7] and psb_route.count((i, j+1)) < 1000:
                dfs(N, M, i, j+1, L-1)
        elif matrix[i][j] == 5:
            if i != N-1 and matrix[i+1][j] in [1, 2, 4, 7] and psb_route.count((i+1, j)) < 1000:
                dfs(N, M, i+1, j, L-1)
            if j != M-1 and matrix[i][j+1] in [1, 3, 6, 7] and psb_route.count((i, j+1)) < 1000:
                dfs(N, M, i, j+1, L-1)
        elif matrix[i][j] == 6:
            if i != N-1 and matrix[i+1][j] in [1, 2, 4, 7] and psb_route.count((i+1, j)) < 1000:
                dfs(N, M, i+1, j, L-1)
            if j != 0 and matrix[i][j-1] in [1, 3, 4, 5] and psb_route.count((i, j-1)) < 1000:
                dfs(N, M, i, j-1, L-1)
        elif matrix[i][j] == 7:
            if i != 0 and matrix[i-1][j] in [1, 2, 5, 6] and psb_route.count((i-1, j)) < 1000:
                dfs(N, M, i-1, j, L-1)
            if j != 0 and matrix[i][j-1] in [1, 3, 4, 5] and psb_route.count((i, j-1)) < 1000:
                dfs(N, M, i, j-1, L-1)

T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    psb_route = []
    dfs(N, M, R, C, L)
    
    print('#{} {}'.format(tc, len(set(psb_route))))