import sys
sys.stdin = open('input.txt')

def f(n, cost):
    global N, min_cost
    if n == N:
        if cost < min_cost:
            min_cost = cost
    elif cost >= min_cost:
        return
    else:
        for i in range(N):
            if col[i] == 0:
                col[i] = 1
                f(n+1, cost+M[n][i])
                col[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    M = [list(map(int, input().split())) for _ in range(N)]
    col = [0]*N
    min_cost = 1000000
    f(0, 0)
    print('#{} {}'.format(tc, min_cost))