def shoot(s, temp, N, M, D):
    minD = D + 1 # 최소 거리값 초기화
    ti, tj = -1, -1 # 화살을 맞는 적의 좌표
    for i in range(N):
        for j in range(M):
            if temp[i][j]>0 and abs(i-N)+abs(j-s)<=D: # 사거리 이내의 적이 있으면
                if minD > abs(i-N)+abs(j-s):
                    ti, tj = i, j
                    minD = abs(i-N)+abs(j-s)
                elif minD == abs(i-N)+abs(j-s) and j < tj:
                    ti, tj = i, j
                    minD = abs(i-N) + abs(j-s)
    if ti >= 0: # 화살의 맞는 적이 있으면
        temp[ti][tj] += 1 # 화살을 맞은 표시를 남김

def defense(s1, s2, s3, N, M, D):
    temp = [[0]*M for _ in range(N)] # 게임판 선언(복사)
    for i in range(N):
        for j in range(M):
            temp[i][j] = enemy[i][j]

    count = 0
    for _ in range(N): # 게임판의 가장 윗 줄의 적까지 공격을 수행했을 때 게임이 끝남
        shoot(s1, temp, N, M, D) # temp에서 화살을 맞은 적은 +1
        shoot(s2, temp, N, M, D)
        shoot(s3, temp, N, M, D)

        for i in range(N):
            for j in range(M):
                if temp[i][j] > 1:
                    temp[i][j] = 0
                    count += 1
        temp = [[0]*M] + temp[:N-1]
    return count

import sys
N, M, D = map(int, sys.stdin.readline().split())
enemy = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
result = []
for i in range(M-2):
    for j in range(i+1, M-1):
        for k in range(j+1, M):
            result.append(defense(i, j, k, N, M, D))
print(max(result))