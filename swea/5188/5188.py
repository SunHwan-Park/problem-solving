import sys
sys.stdin = open('input.txt')

dx = [1, 0]
dy = [0, 1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    result = 100000000000

    queue = [(0, 0, matrix[0][0])]
    while queue:
        ci, cj, cost = queue.pop()
        for k in range(2):
            ni = ci + dx[k]
            nj = cj + dy[k]
            if ni < N and nj < N:
                new_cost = cost+matrix[ni][nj]
                if ni == nj == N - 1:
                    if new_cost < result:
                        result = new_cost
                    break
                elif new_cost < result:
                    queue.append((ni, nj, new_cost))
    print('#{} {}'.format(tc, result))