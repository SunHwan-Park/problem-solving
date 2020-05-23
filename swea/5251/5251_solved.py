import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    V += 1
    adj = {i:[] for i in range(V)}
    for i in range(E):
        s, e, c = map(int, input().split())
        adj[s].append([e, c])
        
    INF = float('inf')
    dist = [INF] * V
    selected = [False] * V
    dist[0] = 0
    cnt = 0
    while cnt < V:
        minV = INF
        u = -1
        for i in range(V):
            if not selected[i] and dist[i] < minV:
                minV = dist[i]
                u = i
        selected[u] = True    
        for w, cost in adj[u]:
            if dist[w] > dist[u] + cost:
                dist[w] = dist[u] + cost
        cnt += 1
    print('#{} {}'.format(tc, dist[V-1]))