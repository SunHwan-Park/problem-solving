import sys
sys.stdin = open('input.txt')

def go(n):
    if n*2 > N:
        return f[n]
    elif n*2 == N:
        return go(n*2)
    elif n*2 <= N-1:
        return go(n*2) + go(n*2+1)
 
T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
 
    f = [0]*(N+1)
    for _ in range(M):
        m, num = map(int, input().split())
        f[m] = num
    print(f'#{tc} {go(L)}')