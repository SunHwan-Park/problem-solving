import sys
sys.stdin = open('input.txt')

def f(n, S):
    global N, K, count
    if S == K:
        count += 1
        return
    elif S > K:
        return
    elif n == N:
        return
    else:
        f(n+1, S+D[n])
        f(n+1, S)

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    D = list(map(int, input().split()))
    count = 0
    f(0, 0)
    print('#{} {}'.format(tc, count))