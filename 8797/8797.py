import sys
sys.stdin = open('input.txt')

# 0. matrix 90도 회전 함수 생성
def rotate_90(matrix):
    N = len(matrix)
    result = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            result[j][N - i - 1] = matrix[i][j]
    return result

# 1. test data 입력
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input().split())))
    
    # 2. 각 구역별 수확량 구하기
    result = []
    for _ in range(4): # 4개의 구역
        carrots = 0
        for i in range(N // 2):
            carrots += sum(matrix[i][i+1:N-i-1])
        result.append(carrots)
        matrix = rotate_90(matrix) # matrix 회전(구역 변경)
    
    # 3. 결과 출력
    print('#{} {}'.format(tc, max(result)-min(result)))