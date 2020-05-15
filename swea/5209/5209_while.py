import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    M = [list(map(int, input().split())) for _ in range(N)]
    min_cost = 1000000
    queue = [(0, 0, [])]
    while queue:
        step, cost, V = queue.pop()
        if step == N:
            if cost < min_cost:
                min_cost = cost
        for i in range(N):
            if i not in V and cost+M[step][i] < min_cost:
                next_V = V[:]
                next_V.append(i)
                queue.append((step+1, cost+M[step][i], next_V))
    print('#{} {}'.format(tc, min_cost))