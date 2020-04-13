import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    D, H, M = list(map(int, input().split()))
    current = 11*24*60 + 11*60 + 11
    sad_time = D*24*60 + H*60 + M
    expect_time = sad_time - current
    if expect_time >= 0:
        print('#{} {}'.format(tc, expect_time))
    else:
        print('#{} {}'.format(tc, -1))