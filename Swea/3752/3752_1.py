# import sys
# sys.stdin = open('input.txt')

from itertools import combinations

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    D = list(map(int, input().split()))
    R = set()
    for i in range(N//2+1):
        for c in combinations(D, i):
            R.add(sum(c))
            temp = D[:]
            for k in c:
                temp.remove(k)
            R.add(sum(temp))
    print('#{} {}'.format(tc, len(R)))