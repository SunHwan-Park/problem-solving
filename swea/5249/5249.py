import sys
sys.stdin = open('input.txt')

import heapq

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    V += 1
    adj = {i: [] for i in range(V)}
    for i in range(E):
        n1, n2, w = map(int, input().split())
        adj[n1].append([n2, w])
        adj[n2].append([n1, w])
    INF = float('inf')
    key = [INF] * V
    mst = [False] * V
    pq = []
    key[0] = 0
    heapq.heappush(pq, (0, 0))
    result = 0
    cnt = 0
    result = 0
    while pq:
        k, node = heapq.heappop(pq)
        if mst[node]: continue
        mst[node] = True
        result += k
        for dest, wt in adj[node]:
            if not mst[dest] and key[dest] > wt:
                key[dest] = wt
                heapq.heappush(pq, (key[dest], dest))
    print('#{} {}'.format(tc, result))