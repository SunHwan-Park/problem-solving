def DFS(n, G, V):
    s = []
    s.append(n) # 시작점 push
    visited[n] = 1
    while len(s) > 0:
        n = s.pop()
        result.append(n)
        if n == G:
            break
        for i in range(1, V+1):
            if adj[n][i] == 1 and visited[i] == 0: #n번 노드에서 갈 수 있는 경로 추가
                s.append(i)
                visited[i] = 1
                if i == G:
                    break

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[0]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        i, j = map(int, input().split())
        adj[i][j] = 1
    visited = [0]*(V+1)
    S, G = map(int, input().split())
    result = []
    DFS(S, G, V)
    if G in result:
        print('#{} {}'.format(tc, 1))
    else:
        print('#{} {}'.format(tc, 0))

# -------------------------------------
# 강사님 코드
def DFS(n, G, V):
    if n == G:
        return 1
    else:
        visited[n] = 1
        for i in range(1, V+1):
            if adj[n][i] == 1 and visited[i] == 0:
                if DFS(i, G, V):
                    return 1
        return 0

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[0]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        i, j = map(int, input().split())
        adj[i][j] = 1
    visited = [0]*(V+1)
    S, G = map(int, input().split())
    print('#{} {}'.format(tc, DFS(S, G, V)))