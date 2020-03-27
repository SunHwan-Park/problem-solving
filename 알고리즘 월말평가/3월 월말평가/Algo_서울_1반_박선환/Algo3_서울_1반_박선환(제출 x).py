import sys
sys.stdin = open('input.txt')

def algo3(matrix, N):
    global result
    if sum([sum(matrix[i]) for i in range(N)]) == N*N:
        result += '1'
        return
    elif sum([sum(matrix[i]) for i in range(N)]) == 0:
        result += '0'
        return
    else:
        result += 'x'
        matrix1 = [matrix[i][:N//2] for i in range(N//2)]
        matrix2 = [matrix[i][N//2:] for i in range(N//2)]
        matrix3 = [matrix[i][:N//2] for i in range(N//2, N)]
        matrix4 = [matrix[i][N//2:] for i in range(N//2, N)]
        algo3(matrix1, N//2)
        algo3(matrix2, N//2)
        algo3(matrix3, N//2)
        algo3(matrix4, N//2)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    M = [list(map(int, input().split())) for _ in range(N)]
    result = ''
    algo3(M, N)
    print(result)