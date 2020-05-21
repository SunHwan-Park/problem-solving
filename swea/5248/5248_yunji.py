import sys
sys.stdin = open('input.txt')

def f(x):
    q = [x]
    while q:
        x = q.pop()
        if not visited[x]:
            visited[x] = 1
            q.extend(nums[x])
T = int(input())
for t in range(1,T+1):
    N, M = map(int, input().split())
    d = list(map(int, input().split()))
    nums = [[] for _ in range(N+1)]
    visited = [0 for _ in range(N+1)]
    for i in range(0, len(d), 2):
        nums[d[i]].append(d[i+1])
        nums[d[i+1]].append(d[i])
    cnt = 0
    for x in range(1, N+1):
        if not visited[x]:
            f(x)
            cnt += 1
    print('#{} {}'.format(t, cnt))