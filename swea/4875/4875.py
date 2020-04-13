import sys
sys.stdin = open('input.txt')

#1. test data 입력
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    M = [list(input()) for _ in range(N)]

    #2. start, end 위치 찾기
    for i in range(N):
        for j in range(N):
            if M[i][j] == '2':
                si, sj = i, j
            if M[i][j] == '3':
                ei, ej = i, j

    #3. 도착점에 도달 할 때 까지 돌아다니기
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    stack = [[si, sj]]

    result = 0
    while stack: # 스택이 빌 때까지
        x, y = stack.pop()
        if (x, y) == (ei, ej): # 해당 위치가 end 점이라면
            result = 1
        else:
            for k in range(4):
                if x+di[k] in range(0, N) and y+dj[k] in range(0, N): # 맵 밖으로 나가지 않고
                    if M[x+di[k]][y+dj[k]] != '1': # 벽이 아니라면
                        stack.append([x+di[k], y+dj[k]]) # 갈 수 있는 모든 길을 스택에 넣어둔다
                        M[x][y] = '1' # 지나간 자리는 벽으로 처리
                        
    # 4. 결과 출력
    print('#{} {}'.format(tc, result))