import sys
sys.stdin = open('input.txt')
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
from itertools import product

def remove(MM, W, H, i, j):
    temp = MM[i][j]
    MM[i][j] = 0
    for k in range(4):
        for l in range(1, temp):
            ni, nj = i+d[k][0]*l, j+d[k][1]*l
            if 0 <= ni < H and 0 <= nj < W and MM[ni][nj] > 0:
                remove(MM, W, H, ni, nj)

T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    M = [list(map(int, input().split())) for _ in range(H)]
    R = W*H
    psb = list(product(range(W), repeat=N))
    for p in psb:
        tmp_M = [[0]*W for _ in range(H)]
        for i in range(H):
            for j in range(W):
                tmp_M[i][j] = M[i][j]
        for col in p:
            for row in range(H):
                if tmp_M[row][col] > 0:
                    sx, sy = row, col
                    break
            remove(tmp_M, W, H, sx, sy)
            for _ in range(H):
                for i in range(H-1):
                    for j in range(W):
                        if tmp_M[i][j] > 0 and tmp_M[i+1][j] == 0:
                            tmp_M[i][j], tmp_M[i+1][j] = tmp_M[i+1][j], tmp_M[i][j]
        count = 0
        for i in range(H):
            for j in range(W):
                if tmp_M[i][j] > 0:
                    count += 1
        if count < R:
            R = count
        if R == 0:
            break
    print('#{} {}'.format(tc, R))