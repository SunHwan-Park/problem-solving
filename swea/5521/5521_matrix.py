import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    R = [[0]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        R[a][b] = 1
        R[b][a] = 1
        
    V = [0]*(N+1)
    friends = []
    cnt = 0
    for i in range(2, N+1):
        if R[1][i] == 1:
            cnt += 1
            V[i] = 1
            friends.append(i)
    for friend in friends:
        for i in range(2, N+1):
            if R[friend][i] == 1 and V[i] == 0:
                cnt += 1
                V[i] = 1
 
    print('#{} {}'.format(tc, cnt))