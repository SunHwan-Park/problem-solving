dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def DFS(i, j):
    visited[i][j] = 1
    for k in range(4):
        ni = i + dx[k]
        nj = j + dy[k]
        if M[ni][nj] != '1' and visited[ni][nj] == 0:
            DFS(ni, nj)

import sys
sys.stdin = open('input.txt')

#1. test data 입력(미로 생성)
for tc in range(1, 11):
    t_num = int(input())
    M = [input() for _ in range(16)]
    visited = [[0]*16 for _ in range(16)]

    #2. start, end 위치 찾기
    for i in range(16):
        for j in range(16):
            if M[i][j] == '2':
                start = [i, j]
            if M[i][j] == '3':
                end = [i, j]
    
    DFS(start[0], start[1])

    if visited[end[0]][end[1]] == 1:
        print('#{} {}'.format(t_num, 1))
    else:
        print('#{} {}'.format(t_num, 0))