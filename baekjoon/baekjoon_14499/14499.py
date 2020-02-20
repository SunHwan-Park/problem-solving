# test data 입력
N, M, x, y, K = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
command = list(map(int, input().split()))

# 현재 바닥의 위치 조정을 위한 di, dj
di = [0, 0, 0, -1, 1]
dj = [0, 1, -1, 0, 0]

# 주사위 위치[0, 위, 북, 동, 서, 남, 아래]
dice = [0]*7

# 각 명령별 주사위 굴리기 수행
for c in command:
    if c == 1 and y != M-1: # 동쪽으로 굴릴 때
        dice[6], dice[4], dice[1], dice[3] = dice[3], dice[6], dice[4], dice[1]
    elif c == 2 and y != 0: # 서쪽으로 굴릴 때
        dice[3], dice[6], dice[4], dice[1] = dice[6], dice[4], dice[1], dice[3]
    elif c == 3 and x != 0: # 북쪽으로 굴릴 때
        dice[2], dice[6], dice[5], dice[1] = dice[1], dice[2], dice[6], dice[5]
    elif c == 4 and x != N-1: # 남쪽으로 굴릴 때
        dice[1], dice[2], dice[6], dice[5] = dice[2], dice[6], dice[5], dice[1]
    else: # 만약 지도의 범위를 넘어선다면
        continue # 아래의 단계 생략

    (x, y) = (x + di[c], y + dj[c]) # 주사위 바닥면 위치 변경
    if matrix[x][y] == 0: # 해당 위치의 숫자가 0이라면
        matrix[x][y] = dice[6] # 주사위 바닥에 있는 숫자를 해당 위치에 복사
    else: # 해당 위치의 숫자가 0이 아니라면
        dice[6] = matrix[x][y] # 해당 위치의 숫자를 주사위 바닥에 복사
        matrix[x][y] = 0 # 해당 위치의 숫자를 0으로 바꿔줌
    print(dice[1]) # 주사위 윗면을 출력