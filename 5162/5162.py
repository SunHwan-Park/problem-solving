import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    A, B, C = list(map(int, input().split()))
    if A > B:
        print('#{} {}'.format(tc, C // B))
    else:
        print('#{} {}'.format(tc, C // A))