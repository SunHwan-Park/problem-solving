import sys
sys.stdin = open('input.txt')
  
def f(n, i, j, s):
    if n == 7:
        t.add(s)
    else:
        for k in range(4):
            ni = i + d[k][0]
            nj = j + d[k][1]
            if 0 <= ni < 4 and 0 <= nj < 4:
                f(n+1, ni, nj, s*10+M[i][j])

d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
T = int(input())
for tc in range(1, T+1):
    M = [list(map(int, input().split())) for _ in range(4)]
    t = set()
    for i in range(4):
        for j in range(4):
            f(0, i, j, 0)
    print('#{} {}'.format(tc, len(t)))