import sys
sys.stdin = open('input.txt')

def f(n, k):
    global cnt
    if n == k:
        cnt += 1
    else:
        f(n+1, k)
        if k - n >= 2:
            f(n+2, k)
            f(n+2, k)

T = int(input())
for tc in range(1, T+1):
    N = int(input())//10
    cnt = 0
    f(0, N)
    print('#{} {}'.format(tc, cnt))