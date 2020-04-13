import sys
sys.stdin = open('input.txt')

# 1. test data 입력
T = 10
for tc in range(1, T+1):
    t_num = int(input())
    matrix = [[0]+list(map(int, input().split()))+[0] for _ in range(100)] # 양 옆으로 가벽(0)을 붙여줌(양쪽 벽 끝에서의 상황을 통제해주기 위해)
    result = []
    
    # 2. 각 시작점에서 도착점까지의 거리 탐색
    for j in range(1, 101):
        i = 0
        current = matrix[i][j] # 현재 위치
        if current == 1: # 해당 지점이 시작점이라면
            distance = 0
            while i != 99: # 도착할 때까지
                if matrix[i][j-1] != 1 and matrix[i][j+1] != 1: # 양 옆에 아무것도 없다면 밑으로 한 칸 이동
                    i += 1
                    distance += 1
                else:
                    if matrix[i][j-1] == 1: # 현재 위치의 왼쪽에 길이 있다면
                        while True:
                            if matrix[i][j-1] == 1 and j != 1: # 왼쪽에 길이 있고, 현재 위치가 왼쪽 끝이 아니라면
                                j -= 1 # 현재 위치에서 한 칸 좌측으로 이동한다
                                distance += 1
                            else: # 왼쪽에 길이 없거나 왼쪽 끝이라면 이동 멈춤
                                break
                        i += 1 # 왼쪽으로 갈 때까지 다 이동했으니 밑으로 한 칸 이동
                        distance += 1
                        if i == 99: # 만약 도착했다면 전체 while 문 끝내기
                            break
                    elif matrix[i][j+1] == 1: # 현재 위치의 오른쪽에 길이 있다면
                        while True:
                            if matrix[i][j+1] == 1 and j != 100: # 오른쪽에 길이 있고, 현재 위치가 오른쪽 끝이 아니라면
                                j += 1 # 현재 위치에서 한 칸 우측으로 이동한다
                                distance += 1
                            else: # 오른쪽에 길이 없거나 오른쪽 끝이라면 이동 멈춤
                                break
                        i += 1 # 오른쪽으로 갈 때까지 다 이동했으니 밑으로 한 칸 이동
                        distance += 1
                        if i == 99: # 만약 도착했다면 전체 while 문 끝내기
                            break

            result.append(distance) # 해당 시작점부터 도착점까지의 거리 추가
        else:
            result.append(10000) # 시작점이 아닌 경우(result의 인덱스을 채우기 위해서)
    
    # 3. 결과물 출력
    r_result = list(reversed(result))
    print('#{} {}'.format(t_num, 99 - r_result.index(min(result))))