# 반복문으로 풀어보자
# N = 4일 때
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    
    for i in range(N):
        matrix = [[0 for _ in range(N)] for _ in range(N)]
        row = [0]*N
        col = [0]*N
        right = [0]*(2*N-1)
        left = [0]*(2*N-1)
        
        matrix[0][i] = 1
        row[0] = 1
        col[i] = 1
        right[0 + i] = 1
        left[0 + N - 1 - i] = 1 
        
        for j in range(N):
            matrix2 = matrix[:]
            row2 = row[:]
            col2 = col[:]
            right2 = right[:]
            left2 = left[:] 
            if row2[1] == 0 and col2[j] == 0 and right2[1 + j] == 0 and left2[1 + N - 1 - j] == 0:
                matrix2[1][j] = 1
                row2[1] = 1
                col2[j] = 1
                right2[1 + j] = 1
                left2[1 + N - 1 - j] = 1
                
                for k in range(N):
                    matrix3 = matrix2[:]
                    row3 = row2[:]
                    col3 = col2[:]
                    right3 = right2[:]
                    left3 = left2[:] 
                    if row3[2] == 0 and col3[k] == 0 and right3[2 + k] == 0 and left3[2 + N - 1 - k] == 0:
                        matrix3[2][k] = 1
                        row3[2] = 1
                        col3[k] = 1
                        right3[2 + k] = 1
                        left3[2 + N - 1 - k] = 1

                        for l in range(N):
                            matrix4 = matrix3[:]
                            row4 = row3[:]
                            col4 = col3[:]
                            right4 = right3[:]
                            left4 = left3[:]
                            if row4[3] == 0 and col4[l] == 0 and right4[3 + l] == 0 and left4[3 + N - 1 - l] == 0:
                                matrix4[3][l] = 1
                                row4[3] = 1
                                col4[l] = 1
                                right4[3 + l] = 1
                                left4[3 + N - 1 - l] = 1
                                print(matrix4)