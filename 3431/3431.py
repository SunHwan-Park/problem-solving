import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    L, U, X = list(map(int, input().split()))
    if X > U:
        answer = -1
    elif X >= L:
        answer = 0
    else:
        answer = L - X
    print('#{} {}'.format(tc, answer))