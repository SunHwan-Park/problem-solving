import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    V, E = list(map(int, input().split()))
    d = list(map(int, input().split()))
    M = [[0 for _ in range(V+1)] for _ in range(V+1)]
    for i in range(E):
        M[d[i*2]][d[i*2+1]] = 1

    t_M = [[0 for _ in range(V+1)] for _ in range(V+1)]
    for i in range(V+1):
        for j in range(V+1):
            t_M[j][i] = M[i][j]

    visited = [0 for _ in range(V+1)]

    first_node = []
    for i in range(V+1):
        if sum(t_M[i]) == 0:
            first_node.append(i)
            visited[i] = 1
    first_node.pop(0)
    visited[0] = 0
    answer = ''
    
    
    min_accept = 1000000
    for i in range(1, V+1):
        if visited[i] != 1:
            if sum(t_M[i]) < min_accept:
                min_accept = sum(t_M[i])

    queue = []
    for node in first_node:
        answer += str(node)+' '
        for i in range(V+1):
            if M[node][i] == 1 and sum(t_M[i]) == min_accept:
                queue.append(i)
                visited[i] = 1
                t_M[i][node] = 0

    while sum(visited) != V or queue:
        min_accept = 1000000
        for i in range(1, V+1):
            if visited[i] != 1:
                if sum(t_M[i]) < min_accept:
                    min_accept = sum(t_M[i])

        for node in sorted(queue):
            answer += str(node)+' '
            for i in range(V+1):
                if M[node][i] == 1 and sum(t_M[i]) == min_accept:
                    queue.append(i)
                    visited[i] = 1
                    t_M[i][node] = 0
            queue.pop(0)
    
    print('#{} {}'.format(tc, answer))