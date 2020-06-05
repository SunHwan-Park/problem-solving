import sys
sys.stdin = open('input.txt')

import heapq

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())
    
    dist = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            dist[i][j] = (X[i] - X[j])**2 + (Y[i] - Y[j])**2

    V = [0]*N
    heap = []
    heapq.heappush(heap, (0, 0))
    INF = float('inf')
    W = [INF]*N
    W[0] = 0

    while heap:
        key, node = heapq.heappop(heap)
        if V[node] == 1:
            continue
        V[node] = 1
        for i in range(N):
            if V[i] == 0:
                if W[i] > dist[node][i]:
                    W[i] = dist[node][i]
                    heapq.heappush(heap, (dist[node][i], i))
    print('#{} {}'.format(tc, round(sum(W)*E)))