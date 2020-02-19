# 재귀 사용
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def DFS(i, j):
    if M[i][j] == '3':
        return 1
    else:
        M[i][j] = '1'
        for k in range(4):
            ni = i + dx[k]
            nj = j + dy[k]
            if M[ni][nj] != '1':
                if DFS(ni, nj) == 1:
                    return 1
        return 0

import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    t_num = int(input())
    M = [list(input()) for _ in range(16)]
    si, sj = -1, -1

    for i in range(16):
        for j in range(16):
            if M[i][j] == '2':
                si, sj = i, j
                break
        if si != -1:
            break
    print('#{} {}'.format(tc, DFS(si, sj)))

# -----------------------------------------
# 반복 사용
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def DFS(i, j):
    s = []
    visited = [[0]*16 for _ in range(16)]
    s.append((i, j))
    visited[i][j] = 1
    while s:
        i, j = s.pop()
        if M[i][j] == '3':
            return 1
        for k in range(4):
            ni = i + dx[k]
            nj = j + dy[k]
            if M[ni][nj] != '1' and visited[ni][nj] == 0: # 벽이 아니고, 방문 안 한 칸이 있으면
                s.append((ni, nj)) # 방문할 칸 목록에 push
                visited[ni][nj] = 1
    return 0 # 목적지에 도착하지 못하는 경우

import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    t_num = int(input())
    M = [list(input()) for _ in range(16)]
    si, sj = -1, -1

    for i in range(16):
        for j in range(16):
            if M[i][j] == '2':
                si, sj = i, j
                break
        if si != -1:
            break
    print('#{} {}'.format(tc, DFS(si, sj)))