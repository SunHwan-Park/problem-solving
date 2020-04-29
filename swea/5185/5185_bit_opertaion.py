import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, V = input().split()
    result = ''
    for num in V:
        num = int(num, 16)
        for i in range(3, -1, -1):
            if num & (1 << i):
                result += '1'
            else:
                result += '0'
    print('#{} {}'.format(tc, result))