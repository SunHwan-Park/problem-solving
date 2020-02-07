import sys
sys.stdin = open('input.txt')

last_date = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
T = int(input())
for tc in range(1, T+1):
    m, d = list(map(int, input().split()))
    print('#{} {}'.format(tc, ((sum(last_date[:m-1]) + d + 3) % 7)))
