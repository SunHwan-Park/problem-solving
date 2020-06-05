import sys
sys.stdin = open('input.txt')

from itertools import combinations

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))

    min_r = 20000000
    for i in range(1, N+1):
        for c in list(combinations(H, i)):
            if sum(c) == B:
                min_r = B
                break
            elif min_r > sum(c) > B:
                min_r = sum(c)
        if min_r == B:
            break
    
    print('#{} {}'.format(tc, min_r-B))              