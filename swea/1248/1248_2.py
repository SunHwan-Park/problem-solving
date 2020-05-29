import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    V, E, num1, num2 = map(int, input().split())
    D = list(map(int, input().split()))
    idx_parents = [0]*(V+1)
    idx_babies = [[] for _ in range(V+1)]
    for i in range(E):
        P = D[2*i]
        B = D[2*i+1]
        idx_parents[B] = P
        idx_babies[P].append(B)

    num_parents = []
    while True:
        new_num1 = idx_parents[num1]
        if new_num1 == 0:
            break
        num_parents.append(new_num1)
        num1 = new_num1

    while True:
        new_num2 = idx_parents[num2]
        if new_num2 in num_parents:
            shared_parent = new_num2
            break
        num2 = new_num2

    cnt = 0
    nodes = [shared_parent]
    while nodes:
        cnt += len(nodes)
        new_nodes = []
        for node in nodes:
            new_nodes += idx_babies[node]
        nodes = new_nodes
    
    print('#{} {} {}'.format(tc, shared_parent, cnt))