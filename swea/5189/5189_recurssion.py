import sys
sys.stdin = open('input.txt')

def f(n, k, c, U):
    global R
    if n == k:
        if U + M[c][0] < R:
            R = U + M[c][0]
    elif U >= R:
        return
    else:
        for i in range(N):
            if V[i] == 0:
                V[i] = 1
                f(n+1, k, i, U + M[c][i])
                V[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    M = [list(map(int, input().split())) for _ in range(N)]
    V = [1]+[0]*(N-1)
    R = 1000000
    f(0, N-1, 0, 0)
    print('#{} {}'.format(tc, R))