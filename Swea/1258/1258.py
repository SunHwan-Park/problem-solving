# import sys
# sys.stdin = open('input.txt')

# T = int(input())
# for tc in range(1, T+1):
#     n = int(input())
#     matrix = []
#     for _ in range(n):
#         matrix.append(''.join(input().split()).split('0'))
#     for i in range(n):
#         for j in range(n):
#                 if matrix[i][j] != '':
#                     for k in range(len(matrix[i][j])):
#                         matrix[i].insert(j+1, '')

#     result = []
#     for i in range(n):
#         for j in range(n):
#             try:
#                 if matrix[i][j] != '':
#                     col = len(matrix[i][j])
#                     row = 1
#                     k = i+1
#                     matrix[i].remove(matrix[i][j])
#                     matrix[i].insert(j, '')
#                     while matrix[k][j] != '' and k != n:
#                         matrix[k].remove(matrix[k][j])
#                         matrix[k].insert(j, '')
#                         k += 1
#                         row += 1
#                     result.append([row, col])
#             except:
#                 pass
    
#     answer = ''
#     for square in sorted(sorted(result), key=lambda x: x[0]*x[1]):
#         answer += '{} {} '.format(square[0], square[1])

#     print('#{} {} {}'.format(tc, len(result), answer))

# --------------------------------------------------
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    result = []
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != 0:
                row = 1
                k = i+1
                while matrix[k][j] != 0 and k != n:
                    row += 1
                    k += 1
                col = 1
                l = j+1
                while matrix[i][l] != 0 and l != n:
                    col += 1
                    l += 1
                for a in range(row):
                    for b in range(col):
                        matrix[i+a][j+b] = 0
                result.append([row, col])
    answer = ''
    for square in sorted(sorted(result), key=lambda x: x[0]*x[1]):
        answer += '{} {} '.format(square[0], square[1])
    print('#{} {} {}'.format(tc, len(result), answer))