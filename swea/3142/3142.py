import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    print('#{} {} {}'.format(tc, 2*M-N, N-M))