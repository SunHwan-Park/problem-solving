import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = list(map(int, input().split()))
    score = list(map(int, input().split()))
    score.sort()
    print('#{} {}'.format(tc, sum(score[N-K:])))