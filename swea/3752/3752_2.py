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
    num_count = {}
    for n in set(D):
        num_count[n] = D.count(n)
    nums = list(num_count.keys())
    R = set()
    f(0, len(num_count), 0)
    print('#{} {}'.format(tc, len(R)))