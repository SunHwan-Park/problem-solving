import sys
sys.stdin = open('input.txt')
  
def f(n, k, i, j, temp):
    if n == k:
        R.add(temp)
        return
    else:
        for l in range(4):
            ni, nj = i+d[l][0], j+d[l][1]
            if 0 <= ni < 4 and 0 <= nj < 4:
                f(n+1, k, ni, nj, temp+M[ni][nj])

T = int(input())
for tc in range(1, T+1):
    M = [input().split() for _ in range(4)]
    R = set()
    d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for i in range(4):
        for j in range(4):
            temp = M[i][j]
            f(0, 6, i, j, temp)
    print('#{} {}'.format(tc, len(R)))