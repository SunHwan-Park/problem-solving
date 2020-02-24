import sys
sys.stdin = open('input.txt')

from itertools import combinations

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    D = list(map(int, input().split()))

    count = 0
    for i in range(1, N+1):
        for combi in list(combinations(D, i)):
            if sum(combi) == K:
                count += 1
    print('#{} {}'.format(tc, count))
    d = 0