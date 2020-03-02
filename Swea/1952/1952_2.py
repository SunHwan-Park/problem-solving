import sys
sys.stdin = open('input.txt')

def dfs(n, s, d, m, t_m):
    global minV
    if n > 11:
        if minV > s:
            minV = s
    elif minV <= s:
        return
    else:
        dfs(n+1, s+min(d*plan[n], m), d, m, t_m)
        dfs(n+3, s+t_m, d, m, t_m)

T = int(input())
for tc in range(1, T+1):
    day, month, t_month, year = map(int, input().split())
    plan = list(map(int, input().split()))
    minV = year
    dfs(0, 0, day, month, t_month)
    print('#{} {}'.format(tc, minV))