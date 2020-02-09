import sys
sys.stdin = open('input.txt')

# 1. test data 입력
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    SP = list(map(int, input().split()))

    # 2. 
    count = 0
    max_len = -1
    max_sum = 0
    i = 0
    temp = 0
    while i != N-1:
        if SP[i+1] > SP[i]:
            i += 1
        else:
            count += 1
            if len(SP[temp:i+1]) >= max_len:
                max_len = len(SP[temp:i+1])
                if sum(SP[temp:i+1]) >= max_sum:
                    max_sum = sum(SP[temp:i+1])
            i += 1
            temp = i
    print(count, max_sum)
