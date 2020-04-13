def f(n, k):
    if n == k:
        B = A[:]
        result.append(B)
        return
    else:
        for i in range(N):
            if used[i] == 0:
                A[n] = i
                used[i] = 1
                f(n+1, k)
                used[i] = 0


import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    M = [list(map(int, input().split())) for _ in range(N)]

    used = [0]*N
    A = [0]*N
    result = []
    f(0, N)
    
    answer = []

    for r in result:
        temp = []
        for i in range(N):
            temp.append(M[i][r[i]])
        answer.append(sum(temp))

    print('#{} {}'.format(tc, min(answer)))