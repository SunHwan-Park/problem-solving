import sys
sys.stdin = open('input.txt')

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
pd = {
    1: [0, 1, 2, 3],
    2: [0, 2],
    3: [1, 3],
    4: [0, 1],
    5: [1, 2],
    6: [2, 3],
    7: [3, 0]
}    

T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    V = [[0]*M for _ in range(N)]
    queue = [(R, C)]
    V[R][C] = 1
    
    while queue:
        CR, CC = queue.pop(0)
        if V[CR][CC] >= L:
            break
        else:
            for i in pd[matrix[CR][CC]]:
                NR = CR + dx[i]
                NC = CC + dy[i]
                if 0 <= NR < N and 0 <= NC < M and V[NR][NC] == 0 and matrix[NR][NC] != 0 and (i + 2)%4 in pd[matrix[NR][NC]]:
                    queue.append((NR, NC))
                    V[NR][NC] = V[CR][CC] + 1

    result = 0
    for i in range(N):
        for j in range(M):
            if V[i][j] > 0:
                result += 1
    print('#{} {}'.format(tc, result))