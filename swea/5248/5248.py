import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    D = list(map(int, input().split()))
    G = [0]*(N+1)
    G_cnt = 0
    S_cnt = N - len(set(D))
    for i in range(M):
        f = D[2*i]
        b = D[2*i+1]
        if G[f] and G[b]:
            c_to = G[f]
            c_from = G[b]
            for j in range(N+1):
                if G[j] == c_from:
                    G[j] = c_to
        elif G[f]:
            G[b] = G[f]
        elif G[b]:
            G[f] = G[b]
        else:
            G_cnt += 1
            G[f] = G_cnt
            G[b] = G_cnt
    print('#{} {}'.format(tc, len(set(G)) - 1 + S_cnt))