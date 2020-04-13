import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    n, b = map(int, input().split())
    hs = list(map(int, input().split()))
    mini = 2147000
    for i in range(1, (1 << n)):
        sum_height = 0
        for j in range(0, n):
            if i & (1 << j):
                sum_height += hs[j]
            if sum_height > mini:
                break
        if sum_height >= b and sum_height < mini:
            mini = sum_height
        if sum_height == b:
            break
    print("#{} {}".format(t, mini - b))