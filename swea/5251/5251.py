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
    heapq.heappush(pq, (0, 0, 0))
    cnt = 0
    final = {i: set() for i in range(V)}
    while pq:
        k, node, frm = heapq.heappop(pq)
        if mst[node]: continue
        final[node].add(frm)
        final[frm].add(node)
        mst[node] = True
        for dest, wt in adj[node]:
            if not mst[dest] and key[dest] > wt:
                key[dest] = wt
                heapq.heappush(pq, (key[dest], dest, node))
    
    visit = [0]*V
    def search(n, lst):
        global V, result
        if result:
            return
        for i in final[n]:
            if i == V-1:
                lst.append((n, V-1))
                result = lst[:]
                break
            elif visit[i] == 0:
                visit[i] = 1
                lst.append((n, i))
                search(i, lst)
                visit[i] = 0

    visit[0] = 1
    result = None
    search(0, [])
    answer = 0
    for n1, n2 in result:
        for node, wt in adj[n1]:
            if node == n2:
                answer += wt
                break
    print('#{} {}'.format(tc, answer))