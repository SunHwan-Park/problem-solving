import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    print('#{}'.format(tc), end=' ')
    for _ in range(N):
        print('1/{}'.format(N), end=' ')
    print()