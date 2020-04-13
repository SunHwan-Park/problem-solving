def f(n, k, min_sum):
    if n == k:
        if sum(sum_temp) < min_sum[0]:
            min_sum[0] = sum(sum_temp)
            return
        return
    else:
        for i in range(N):
            if used[i] == 0:
                A.append(i)
                used[i] = 1
                sum_temp.append(M[i][A[i]])
                if sum(sum_temp) >= min_sum[0]:
                    sum_temp.pop()
                    return
                f(n+1, k, min_sum)
                used[i] = 0
                A.pop()


import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    M = [list(map(int, input().split())) for _ in range(N)]

    min_sum = [1000000000]
    sum_temp = []
    A = []
    used = [0]*N
    result = []
    f(0, N, min_sum)


    print('#{} {}'.format(tc, min(answer)))