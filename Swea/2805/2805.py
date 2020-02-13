import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = []
    for _ in range(N):
        matrix.append(input())
    for i in range(N//2):
        matrix[i] = matrix[i][N//2 - i:N//2 + i + 1]
        matrix[N-i-1] = matrix[N-i-1][N//2 - i:N//2 + i + 1]
    result = 0
    for i in range(N):
        for n in matrix[i]:
            result += int(n)

    print('#{} {}'.format(tc, result))