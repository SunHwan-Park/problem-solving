import sys
sys.stdin = open('input.txt')

# 1. test data 입력
T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    matrix = [[-1 for _ in range(N+2)] for _ in range(N+2)] # 편의상 사방으로 한칸씩 더 늘려서 판 짜기(빈 공간은 10으로)
    # 매트릭스 가운데 시작 돌 놓기
    matrix[N//2][N//2], matrix[N//2 + 1][N//2 + 1] = 2, 2 # 백돌
    matrix[N//2][N//2 + 1], matrix[N//2 + 1][N//2] = 1, 1 # 흑돌
    
    # 2. 한 수의 정보 입력
    for _ in range(M):
        col, row, color = list(map(int, input().split()))
        # 2_1. 입력에 따라 돌을 놓기
        matrix[row][col] = color
        # 2_2. 놓은 돌의 주변을 탐색하기
        for i in range(-1, 2):
            for j in range(-1, 2):
                # 2_3. 주변에 상대의 돌이 있다면
                if abs(color - matrix[row+i][col+j]) == 1:
                    temp = []
                    ii = i
                    jj = j
                    # 2_4. 해당 방향으로 한 칸씩 증가시키며 좌표를 저장하기
                    while abs(color - matrix[row+ii][col+jj]) == 1:
                        temp.append([ii, jj])
                        ii += i
                        jj += j
                    # 2_5. 그 끝에 나의 돌이 있다면, 저장해둔 좌표들을 나의 돌로 바꾸기
                    if matrix[row+ii][col+jj] == color:
                        for k, m in temp:
                            matrix[row+k][col+m] = color

    # 3. 전체 판에서 백돌, 흑돌 개수 세기
    white = 0
    black = 0
    for line in matrix:
        white += line.count(2)
        black += line.count(1)

    # 4. 결과 출력
    print('#{} {} {}'.format(tc, black, white))