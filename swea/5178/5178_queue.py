import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    V = [0]*(N+1)
    queue = []
    for _ in range(M):
        node, value = map(int, input().split())
        V[node] = value
        queue.append(node)
    while queue:
        leaf = queue.pop(0)
        parent = leaf//2
        V[parent] += V[leaf]
        if parent not in queue and parent != 0:
            queue.append(parent)
    print('#{} {}'.format(tc, V[L]))