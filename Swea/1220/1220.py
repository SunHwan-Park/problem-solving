import sys
sys.stdin = open('input.txt')

# 1. test data 입력
T = 10
for tc in range(1, T+1):
    n = int(input())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))
    
    # 2. 매트릭스 90도 회전(계산 편의를 위해)
    matrix_90 = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            matrix_90[j][n-i-1] = matrix[i][j]

    # 3. 양 끝에 떨어질 수 있는 자성체 제거
    for i in range(n):
        for j in range(n):
            if matrix_90[i][j] == 1:
                matrix_90[i][j] = 0
            elif matrix_90[i][j] == 2:
                break
        for k in range(n-1, -1, -1):
            if matrix_90[i][k] == 2:
                matrix_90[i][k] = 0
            elif matrix_90[i][k] == 1:
                break
    
    # 4. 교착 상태 수 세기
    answer = 0
    for i in range(n):
        temp = ''.join(map(str, matrix_90[i])).replace('0', '')
        answer += temp.count('21') # 결국 하나의 교착 상태에는 '21'이 담겨져 있음

    # 5. 출력
    print('#{} {}'.format(tc, answer))