import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, A, B = map(int, input().split())
    R = int(N**(0.5))
    C = N // R
    min_r = B * (N - R * R)
    while R != 1:
        now_r = A * abs(R - C) + B * (N - R * C)
        if now_r < min_r:
            min_r = now_r
        R -= 1
        C = N // R
    print('#{} {}'.format(tc, min_r))