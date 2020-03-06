# import sys
# sys.stdin = open('input.txt')

def f(n, k, current):
    if n == k:
        R.add(current)
        return
    else:
        for i in range(0, nums[n]*num_count[nums[n]]+1, nums[n]):
            f(n+1, k, current+i)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    D = list(map(int, input().split()))
    decimal = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    d_nums = []
    for n in D:
        if n == 1:
            d_nums.append(n)
        else:
            while n > 1:
                for i in decimal:
                    if n % i == 0:
                        d_nums.append(i)
                        n //= i
                        break
    
    num_count = {}
    for n in set(d_nums):
        num_count[n] = d_nums.count(n)
    nums = list(num_count.keys())
    R = set()
    f(0, len(num_count), 0)
    print('#{} {}'.format(tc, len(R)))