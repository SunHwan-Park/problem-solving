import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    SP = list(map(int, input().split()))+[-1]

    count = 0
    max_len = 0
    max_sum = 0
    i = 0
    temp = 0
    while i != N:
        if SP[i+1] > SP[i]:
            i += 1
        else:
            if len(SP[temp:i+1]) >= 2:
                count += 1
                if len(SP[temp:i+1]) > max_len:
                    max_len = len(SP[temp:i+1])
                    max_sum = sum(SP[temp:i+1])
                elif len(SP[temp:i+1]) == max_len:
                    if sum(SP[temp:i+1]) > max_sum:
                        max_sum = sum(SP[temp:i+1])
            i += 1
            temp = i
    print('#{} {} {}'.format(tc, count, max_sum))