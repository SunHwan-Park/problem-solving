import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**6)

def f(M, N, i, j, cnt, ii, jj):
    if i != 0 and M[i-1][j] == M[i][j]+1:
            f(M, N, i-1, j, cnt+1, ii, jj)
    elif i != N-1 and M[i+1][j] == M[i][j]+1:
            f(M, N, i+1, j, cnt+1, ii, jj)
    elif j != 0 and M[i][j-1] == M[i][j]+1:
            f(M, N, i, j-1, cnt+1, ii, jj)
    elif j != N-1 and M[i][j+1] == M[i][j]+1:
            f(M, N, i, j+1, cnt+1, ii, jj)
    if cnt > result[1]:
        result[0] = M[ii][jj]
        result[1] = cnt
    elif cnt == result[1] and M[ii][jj] < result[0]:
        result[0] = M[ii][jj]
        result[1] = cnt

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    M = []
    for _ in range(N):
        M.append(list(map(int, input().split())))
    result = [N*N+1, 0]
    for i in range(N):
        for j in range(N):
            f(M, N, i, j, 1, i, j)
    print('#{} {} {}'.format(tc, result[0], result[1]))