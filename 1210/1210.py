import sys
sys.stdin = open('input.txt')

# 1. test data 입력
T = 10
for tc in range(1, T+1):
    t_num = int(input())
    matrix = [[0]+list(map(int, input().split()))+[0] for _ in range(100)] # 양 옆으로 가벽(0)을 붙여줌(양쪽 벽 끝에서의 상황을 통제해주기 위해)
    result = []
    
    # 2. 각 시작점에서 도착점까지의 거리 탐색
    for k in range(1, 101):
        i = 0
        j = k
        current = matrix[i][j] # 현재 위치
        if current == 1: # 해당 지점이 시작점이라면
            while i != 99: # 도착할 때까지
                if matrix[i][j-1] != 1 and matrix[i][j+1] != 1: # 양 옆에 아무것도 없다면 밑으로 한 칸 이동
                    i += 1
                else:
                    if matrix[i][j-1] == 1: # 현재 위치의 왼쪽에 길이 있다면
                        while True:
                            if matrix[i][j-1] == 1 and j != 1: # 왼쪽에 길이 있고, 현재 위치가 왼쪽 끝이 아니라면
                                j -= 1 # 현재 위치에서 한 칸 좌측으로 이동한다
                            else: # 왼쪽에 길이 없거나 왼쪽 끝이라면 이동 멈춤
                                break
                        i += 1 # 왼쪽으로 갈 때까지 다 이동했으니 밑으로 한 칸 이동
                        if i == 99: # 만약 도착했다면 전체 while 문 끝내기
                            break
                    elif matrix[i][j+1] == 1: # 현재 위치의 오른쪽에 길이 있다면
                        while True:
                            if matrix[i][j+1] == 1 and j != 100: # 오른쪽에 길이 있고, 현재 위치가 오른쪽 끝이 아니라면
                                j += 1 # 현재 위치에서 한 칸 우측으로 이동한다
                            else: # 오른쪽에 길이 없거나 오른쪽 끝이라면 이동 멈춤
                                break
                        i += 1 # 오른쪽으로 갈 때까지 다 이동했으니 밑으로 한 칸 이동
                        if i == 99: # 만약 도착했다면 전체 while 문 끝내기
                            break
            if matrix[i][j] == 2: # 도착점이 2라면!
                result = k - 1
        else:
            pass
    
    # 3. 결과물 출력
    print('#{} {}'.format(t_num, result))

# ---------------------------------------------------

# 참고 방대승씨 코드
def s(l):
    for i in range(100):
        if l[99][i]==2:x=i;break
    for i in range(98,0,-1):
        if x>0 and l[i][x-1]:
            while l[i][x-1] and x>0:x-=1
        elif x<99 and l[i][x+1]:
            while x<99 and l[i][x+1]:x+=1
    return x
for i in range(10):print("#"+input(),s([list(map(int,input().split())) for i in range(100)]))