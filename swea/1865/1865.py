import sys
sys.stdin = open('input.txt')

def f(n, k, current):
    global result
    if n == k:
        if current > result:
            result = current
        return
    elif current <= result:
        return
    else:
        for j in range(N):
            if V[j] != 1:
                V[j] = 1
                f(n+1, k, current*P[n][j]/100)
                V[j] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]
    result = -1
    V = [0]*N
    f(0, N, 1)
    print('#{} {}'.format(tc, format(result*100, '.6f')))