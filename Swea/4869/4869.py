import sys
sys.stdin = open('input.txt')

def f(n, k):
    if n == k:
        possible.append(space[:])
    else:
        space[n] = 1
        f(n+1, k)
        space[n] = 0

        if k - n >= 2:
            space[n] = 2
            space[n+1] = 0
            f(n+2, k)
            space[n] = 0
            space[n+1] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())//10
    possible = []
    space = [0]*N
    f(0, N)
    cnt = 0
    for p in possible:
        cnt += 2**p.count(2)
    print('#{} {}'.format(tc, cnt))