import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    temp = round(N**(1/3))
    result = -1
    for i in [-1, 0, 1]:
        if (temp+i)**3 == N and temp+i > 0:
            result = temp+i
    print('#{} {}'.format(tc, result))