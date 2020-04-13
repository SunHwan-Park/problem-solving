import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    D = [list(map(lambda x: (x+1)//2, map(int, input().split()))) for _ in range(N)]
    V = [0]*201
    for d in D:
        if d[0] <= d[1]:
            a = d[0]
            b = d[1]
       	else:
            b = d[0]
            a = d[1]
        for i in range(a, b+1):
            V[i] += 1
    print('#{} {}'.format(tc, max(V)))