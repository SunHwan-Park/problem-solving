import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M, K, H = list(map(int, input().split()))
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input().split())))
    
    count = 0
    for i in range(1, N-1):
        for j in range(1, M-1):
            temp = []
            for k in range(-1, 2):
                for l in range(-1, 2):
                    temp.append(matrix[i+k][j+l])
            temp.remove(matrix[i][j])
    
            if max(temp) - min(temp) <= K and H >= matrix[i][j] - min(temp) >= 0:
                count += 1
    
    print('#{} {}'.format(tc, count))