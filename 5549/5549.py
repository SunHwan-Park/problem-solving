import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    if n % 2:
        print('#{} Odd'.format(tc))
    else:
        print('#{} Even'.format(tc))