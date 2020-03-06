import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    D = list(map(int, input().split()))
    S = set((0,))
    for n in D:
        t = set()
        for e in S:
            t.add(e+n)
        S |= t
    print('#{} {}'.format(tc, len(S)))