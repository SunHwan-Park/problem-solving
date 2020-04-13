import sys
sys.stdin = open('input.txt')
def f(node, count):
    global G, result
    if node == G:
        if count < result:
            result = count
    elif count >= result:
        return
    else:
        for i in range(1, V+1):
            if visit[i] == 0 and M[node][i] == 1:
                visit[i] = 1
                f(i, count+1)
                visit[i] = 0

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
    result = V+1
    f(S, 0)
    if result == V+1:
        print('#{} 0'.format(tc))
    else:
        print('#{} {}'.format(tc, result))