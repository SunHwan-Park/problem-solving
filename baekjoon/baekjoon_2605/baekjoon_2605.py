n = int(input())
nums = list(map(int, input().split()))
result = []
for s in range(1, n+1):
    result.insert(s-1-nums[s-1], s)
print(' '.join(map(str, result)))