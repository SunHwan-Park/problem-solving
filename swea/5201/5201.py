import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    W = sorted(list(map(int, input().split())))
    T = sorted(list(map(int, input().split())))
    R = 0
    while W and T:
        goods = W.pop()
        if T[-1] >= goods:
            R += goods
            T.pop()
    
    print('#{} {}'.format(tc, R))