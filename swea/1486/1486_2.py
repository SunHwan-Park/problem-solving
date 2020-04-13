import sys
sys.stdin = open('input.txt')

def dfs(H, B, N, current, i):
    global min_r
    if current >= B or i == N:
        if min_r > current >= B:
            min_r = current
        return
    else:
        dfs(H, B, N, current+H[i], i+1)
        dfs(H, B, N, current, i+1)

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))
    min_r = N*10000
    dfs(H, B, N, 0, 0)
    print('#{} {}'.format(tc, min_r-B))