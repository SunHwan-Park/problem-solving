import sys
sys.stdin = open('s_input.txt')

def rotate(matrix, angle):
    n = len(matrix)
    r_matrix = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if angle == 90:
                r_matrix[j][n-1-i] = matrix[i][j]
            elif angle == 270:
                r_matrix[n-1-j][i] = matrix[i][j]
            elif angle == 180:
                r_matrix[n-1-i][n-1-j] = matrix[i][j]
            elif angle == 'reverse':
                r_matrix[i][n-1-j] = matrix[i][j]
    return r_matrix

def game_right(matrix, N):
    result = []
    for i in range(N):
        line = matrix[i][:]
        while 0 in line:
            line.remove(0)
        for k in range(len(line)-1, 0, -1):
            if line[k] == line[k-1]:
                line[k] = line[k]*2
                line[k-1] = -1
        while -1 in line:
            line.remove(-1)
        while len(line) < N:
            line.insert(0, 0)
        result.append(line)
    return result

T = int(input())
for tc in range(1, T+1):
    print('#{}'.format(tc))
    N, S = input().split()
    N = int(N)
    matrix = [list(map(int, input().split())) for _ in range(N)]

    if S == 'right':
        result = game_right(matrix, N)
        for line in result:
            print(' '.join(map(str, line)))
        
    if S == 'left':
        matrix = rotate(matrix, 'reverse')
        result = rotate(game_right(matrix, N), 'reverse')
        for line in result:
            print(' '.join(map(str, line)))
    
    if S == 'up':
        matrix = rotate(matrix, 90)
        result = rotate(game_right(matrix, N), 270)
        for line in result:
            print(' '.join(map(str, line)))

    if S == 'down':
        matrix = rotate(matrix, 270)
        result = rotate(game_right(matrix, N), 90)
        for line in result:
            print(' '.join(map(str, line)))