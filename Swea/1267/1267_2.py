import sys
sys.stdin = open('input.txt')

# test data 입력
for tc in range(1, 11):
    V, E = list(map(int, input().split()))
    d = list(map(int, input().split()))
    # 인접행렬 생성
    M = [[0 for _ in range(V+1)] for _ in range(V+1)]
    for i in range(E):
        M[d[i*2]][d[i*2+1]] = 1
    # transposed 인접행렬 생성 
    t_M = [[0 for _ in range(V+1)] for _ in range(V+1)]
    for i in range(V+1):
        for j in range(V+1):
            t_M[j][i] = M[i][j]

    # 각 노드의 방문 여부
    visited = [0 for _ in range(V+1)]

    # 최종 결과물
    answer = ''
    
    queue = []
    for i in range(1, V+1):
        if sum(t_M[i]) == 0:
            start_queue.append(i)
            visited[i] = 1
            answer += str(i)+' '
                
    while True:
        if sum(visited[1:]) == V and len(queue) == 0:
            break

        for i in queue:
            for j in range(1, V+1):
                if M[i][j] == 1:
                    


        min_accept = 1000000
        for i in range(1, V+1):
            if visited[i] != 1: # 방문하지 않은 노드 중에서
                if sum(t_M[i]) < min_accept: # 해당 노드로 들어오는 노드의 수가 가장 작다면
                    min_accept = sum(t_M[i])

        for i in range(1, V+1):
            if visited[i] != 1:
                if sum(t_M[i]) == min_accept:
                    stack.append(i)
                    visited[i] = 1
                    answer += str(i)+' '
    
    print('#{} {}'.format(tc, answer))