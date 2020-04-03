import sys
sys.stdin = open('input.txt')
def bfs():
    while queue:
        C = queue.pop(0)
        for i in range(1, V+1):
            if visit[i] == 0 and M[C][i] == 1:
                if i == G:
                    return visit[C]
                else:
                    queue.append(i)
                    visit[i] = visit[C] + 1
    return 0

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    M = [[0]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        D = list(map(int, input().split()))
        M[D[0]][D[1]] = 1
        M[D[1]][D[0]] = 1
    S, G = map(int, input().split())
    visit = [0]*(V+1)
    queue = [S]
    visit[S] = 1
    print('#{} {}'.format(tc, bfs()))