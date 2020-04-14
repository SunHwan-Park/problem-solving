import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    D = list(map(int, input().split()))
    nodes = [[] for _ in range(E+2)]
    for i in range(E):
        nodes[D[i*2]].append(D[i*2+1])
    cnt = 0
    queue = [N]
    while queue:
        cnt += 1
        parent = queue.pop(0)
        for i in nodes[parent]:
            queue.append(i)
    print('#{} {}'.format(tc, cnt))