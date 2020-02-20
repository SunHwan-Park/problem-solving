def change(numbers, two_nums, count):
    global max_num
    global N
    if count == 0:
        temp = numbers[:]
        if max_num < int(''.join(temp)):
            max_num = int(''.join(temp))
        return
    elif ''.join(numbers) < str(max_num)[:N - count]:
        return
    else:
        temp = numbers[:]
        for two_num in two_nums:
            temp[two_num[0]], temp[two_num[1]] = temp[two_num[1]], temp[two_num[0]]
            change(temp, two_nums, count-1)
    
import sys
sys.stdin = open('input.txt')

from itertools import combinations

T = int(input())
for tc in range(1 ,T+1):
    numbers, count = input().split()
    numbers = list(numbers)
    count = int(count)
    N = len(numbers)
    
    two_nums = list(combinations(list(range(len(numbers))), 2))
    max_num = 0
    change(numbers, two_nums, count)
    
    print('#{} {}'.format(tc, max_num))