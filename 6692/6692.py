import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    answer = 0
    for _ in range(N):
        p, x = list(map(float, input().split()))
        answer += p * x
    print('#{} {}'.format(tc, answer))