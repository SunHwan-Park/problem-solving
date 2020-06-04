import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    R = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        R[a].append(b)
        R[b].append(a)
    
    V = [0]*(N+1)
    V[1] = 1
    cnt = len(R[1])
    for i in R[1]:
        V[i] = 1
    for i in R[1]:
        for j in R[i]:
            if V[j] == 0:
                cnt += 1
                V[j] = 1

    print('#{} {}'.format(tc, cnt))