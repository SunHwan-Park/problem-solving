import sys
sys.stdin = open('input.txt')

def dfs(node, V, k):
    global G
    global result
    if node == G:
        result = 1
        return
    elif k == V:
        return
    else:
        for i in range(V+1):
            if M[node][i] == 1 and visit[i] == 0:
                visit[i] = 1
                dfs(i, V, k+1)
                visit[i] = 0

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    M = [[0]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        start, end = map(int, input().split())
        M[start][end] = 1
    S, G = map(int, input().split())
    visit = [0]*(V+1)
    visit[S] = 1
    result = 0
    dfs(S, V, 1)
    
    print('#{} {}'.format(tc, result))