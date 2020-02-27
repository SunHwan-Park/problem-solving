import sys
sys.stdin = open('input.txt')

def dfs(M, i, j, matrix, route, c):
    global count
    if c == len(route):
        count += 1
        return
    else:
        stack = []
        if i != M-1 and matrix[i+1][j] == route[c]:
            stack.append([i+1, j])
        if i != 0 and matrix[i-1][j] == route[c]:
            stack.append([i-1, j])
        if j != M-1 and matrix[i][j+1] == route[c]:
            stack.append([i, j+1])
        if j != 0 and matrix[i][j-1] == route[c]:
            stack.append([i, j-1])

        matrix[i][j] = 0
        
        for s in stack:
            dfs(M, s[0], s[1], matrix, route, c+1)
        else:
            matrix[i][j] = route[c-1]
            return

T = int(input())
for tc in range(1, T+1):
    D = list(map(int, input().split()))
    N = D[0]
    route = D[1:]
    M = int(input())
    matrix = []
    for _ in range(M):
        matrix.append(list(map(int, input().split())))

    start = []
    for i in range(M):
        for j in range(M):
            if matrix[i][j] == route[0]:
                start.append([i, j])
    
    count = 0
    for s in start:
        dfs(M, s[0], s[1], matrix, route, 1)

    print('#{} {}'.format(tc, int(bool(count))))