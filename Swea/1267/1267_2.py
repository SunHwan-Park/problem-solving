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

    visited = [0 for _ in range(V+1)] # 각 노드의 방문 여부
    answer = '' # 최종 결과물
    queue = []
    for i in range(1, V+1):
        if sum(t_M[i]) == 0:
            queue.append(i) # 최초 시작 node를 queue에 넣어준다
  
    while True:
        if sum(visited) == V and len(queue) == 0: # 종료 조건
            break
        for _ in range(len(queue)):
            i = queue.pop(0) # 한 노드씩 방문
            visited[i] = 1
            answer += str(i)+' '
            for j in range(1, V+1):
                if M[i][j] == 1: # 현재 노드와 연결되어 있고
                    t_M[j][i] = 0
                    if sum(t_M[j]) == 0: # 해당 노드로 들어오는 다른 노드가 없다면
                        queue.append(j) # queue에 추가
    
    # 결과 출력
    print('#{} {}'.format(tc, answer))