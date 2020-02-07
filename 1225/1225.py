import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    t_num = int(input())
    numbers = list(map(int, input().split()))
    while numbers[-1] > 0:
        for i in range(1, 6):
            numbers.append(numbers.pop(0)-i)
            if numbers[-1] <= 0:
                numbers[-1] = 0
                break
    print('#{} {}'.format(tc, ' '.join(map(str, numbers))))