def f(n, k):
    global min_sum
    if n == k:
        if sum(sum_temp) < min_sum:
            min_sum = sum(sum_temp)
        return
    elif sum(sum_temp) >= min_sum:
        return
    else:
        for i in range(N):
            if used[i] == 0:
                used[i] = 1
                sum_temp[n] = M[n][i]
                f(n+1, k)
                used[i] = 0
                sum_temp[n] = 0

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    M = [list(map(int, input().split())) for _ in range(N)]
    min_sum = 10000000
    sum_temp = [0]*N
    used = [0]*N
    f(0, N)
    print('#{} {}'.format(tc, min_sum))