import sys
sys.stdin = open('input.txt')

from itertools import combinations

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    M = [list(map(int, input().split())) for _ in range(N)]
    result = 100000000
    L = list(combinations(list(range(N)), N//2))
    for c in L[:len(L)//2]:
        temp1 = 0
        for i in c:
            for j in c:
                temp1 += M[i][j]
        o = set(range(N)) - set(c)
        temp2 = 0
        for i in o:
            for j in o:
                temp2 += M[i][j]
        if abs(temp1 - temp2) < result:
            result = abs(temp1 - temp2)
    print('#{} {}'.format(tc, result))