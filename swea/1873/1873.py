import sys
sys.stdin = open('input.txt')

# 1. test data 입력
T = int(input())
for tc in range(1, T+1):
    H, W = map(int, input().split())
    # game map 생성
    M = []
    for _ in range(H):
        M.append(list(input()))
    N = int(input())
    command = input()

    # 2. 현재 전차의 위치와 방향 파악
    for i in range(H):
        for j in range(W):
            if M[i][j] in ['^', 'v', '<', '>']:
                loc = [i, j]
                if M[i][j] == '^':
                    d = 'up'
                elif M[i][j] == 'v':
                    d = 'down'
                elif M[i][j] == '<':
                    d = 'left'
                else:
                    d = 'right'

    # 3. 각 명령 결과 업데이트
    for i in range(N):
        if command[i] == 'U':
            d = 'up'
            M[loc[0]][loc[1]] = '^'
            if loc[0] - 1 >= 0:
                if M[loc[0]-1][loc[1]] == '.':
                    M[loc[0]][loc[1]], M[loc[0]-1][loc[1]] = M[loc[0]-1][loc[1]], M[loc[0]][loc[1]]
                    loc[0] -= 1
        elif command[i] == 'D':
            d = 'down'
            M[loc[0]][loc[1]] = 'v'
            if loc[0] + 1 < H:
                if M[loc[0]+1][loc[1]] == '.':
                    M[loc[0]][loc[1]], M[loc[0]+1][loc[1]] = M[loc[0]+1][loc[1]], M[loc[0]][loc[1]]
                    loc[0] += 1
        elif command[i] == 'L':
            d = 'left'
            M[loc[0]][loc[1]] = '<'
            if loc[1] - 1 >= 0:
                if M[loc[0]][loc[1]-1] == '.':
                    M[loc[0]][loc[1]], M[loc[0]][loc[1]-1] = M[loc[0]][loc[1]-1], M[loc[0]][loc[1]]
                    loc[1] -= 1
        elif command[i] == 'R':
            d = 'right'
            M[loc[0]][loc[1]] = '>'
            if loc[1] + 1 < W:
                if M[loc[0]][loc[1]+1] == '.':
                    M[loc[0]][loc[1]], M[loc[0]][loc[1]+1] = M[loc[0]][loc[1]+1], M[loc[0]][loc[1]]
                    loc[1] += 1
        elif command[i] == 'S':
            shoot_loc = loc[:]
            if d == 'up':
                while M[shoot_loc[0]][shoot_loc[1]] not in ['*', '#']:
                    if shoot_loc[0]-1 >= 0:
                        shoot_loc[0] -= 1
                    else:
                        break
                if M[shoot_loc[0]][shoot_loc[1]] == '*':
                    M[shoot_loc[0]][shoot_loc[1]] = '.'
            elif d == 'down':
                while M[shoot_loc[0]][shoot_loc[1]] not in ['*', '#']:
                    if shoot_loc[0]+1 < H:
                        shoot_loc[0] += 1
                    else:
                        break
                if M[shoot_loc[0]][shoot_loc[1]] == '*':
                    M[shoot_loc[0]][shoot_loc[1]] = '.'
            elif d == 'left':
                while M[shoot_loc[0]][shoot_loc[1]] not in ['*', '#']:
                    if shoot_loc[1]-1 >= 0:
                        shoot_loc[1] -= 1
                    else:
                        break                    
                if M[shoot_loc[0]][shoot_loc[1]] == '*':
                    M[shoot_loc[0]][shoot_loc[1]] = '.'
            elif d == 'right':
                while M[shoot_loc[0]][shoot_loc[1]] not in ['*', '#']:
                    if shoot_loc[1]+1 < W:
                        shoot_loc[1] += 1
                    else:
                        break                    
                if M[shoot_loc[0]][shoot_loc[1]] == '*':
                    M[shoot_loc[0]][shoot_loc[1]] = '.'
    
    # 4. 결과 출력
    result = ''
    for i in range(H):
        result += ''.join(M[i])+'\n'
    print('#{} {}'.format(tc, result.strip()))


# ----------------------------------------------
# Dev.J 코드
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
 
def shoot(i, j, d):
    y, x = i, j
    while True:
        y += di[d]
        x += dj[d]
        if 0 <= x < W and 0 <= y < H:
            if arr[y][x] == '#':
                return
            elif arr[y][x] == '*':
                arr[y][x] = '.'
                return
        else:
            return
 
T = int(input())
for t in range(1, T+1):
    H, W = map(int, input().split())
    arr = [list(map(str, input())) for _ in range(H)]
    N = int(input())
    C = input() #Command
 
    tank = '^>v<'
    tank_dir = {'^': 0, '>': 1, 'v': 2, '<': 3}
    for i in range(H):
        for j in range(W):
            if arr[i][j] in tank:
                tank_idx = [i, j, tank_dir[arr[i][j]]]
                arr[i][j] = '.'
 
    move = 'URDL' #방향을 해당 방향으로 바꾸고, 전진 가능하면 전진
    for i in range(N):
        if C[i] == 'S':
            shoot(tank_idx[0], tank_idx[1], tank_idx[2])
        else:
            for j in range(len(move)):
                if C[i] == move[j]:
                    my = tank_idx[0]+di[j]
                    mx = tank_idx[1]+dj[j]
                    if 0 <= my < H and 0 <= mx < W:
                        if arr[my][mx] == '.':
                            tank_idx[0] += di[j]
                            tank_idx[1] += dj[j]
                    tank_idx[2] = j
    arr[tank_idx[0]][tank_idx[1]] = tank[tank_idx[2]]
    print("#"+str(t), end=" ")
    for i in range(len(arr)):
        print(''.join(arr[i]))