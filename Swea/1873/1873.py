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
            try:
                if M[loc[0]-1][loc[1]] == '.':
                    M[loc[0]][loc[1]], M[loc[0]-1][loc[1]] = M[loc[0]-1][loc[1]], M[loc[0]][loc[1]]
                    loc[0] -= 1
            except:
                pass
        elif command[i] == 'D':
            d = 'down'
            M[loc[0]][loc[1]] = 'v'
            try:
                if M[loc[0]+1][loc[1]] == '.':
                    M[loc[0]][loc[1]], M[loc[0]+1][loc[1]] = M[loc[0]+1][loc[1]], M[loc[0]][loc[1]]
                    loc[0] += 1
            except:
                pass
        elif command[i] == 'L':
            d = 'left'
            M[loc[0]][loc[1]] = '<'
            try:
                if M[loc[0]][loc[1]-1] == '.':
                    M[loc[0]][loc[1]], M[loc[0]][loc[1]-1] = M[loc[0]][loc[1]-1], M[loc[0]][loc[1]]
                    loc[1] -= 1
            except:
                pass
        elif command[i] == 'R':
            d = 'right'
            M[loc[0]][loc[1]] = '>'
            try:
                if M[loc[0]][loc[1]+1] == '.':
                    M[loc[0]][loc[1]], M[loc[0]][loc[1]+1] = M[loc[0]][loc[1]+1], M[loc[0]][loc[1]]
                    loc[1] += 1
            except:
                pass
        elif command[i] == 'S':
            shoot_loc = loc[:]
            if d == 'up':
                while M[shoot_loc[0]][shoot_loc[1]] not in ['*', '#']:
                    try:
                        M[shoot_loc[0]-1][shoot_loc[1]] = M[shoot_loc[0]-1][shoot_loc[1]]
                    except:
                        break
                    shoot_loc[0] -= 1
                if M[shoot_loc[0]][shoot_loc[1]] == '*':
                    M[shoot_loc[0]][shoot_loc[1]] = '.'
            elif d == 'down':
                while M[shoot_loc[0]][shoot_loc[1]] not in ['*', '#']:
                    try:
                        M[shoot_loc[0]+1][shoot_loc[1]] = M[shoot_loc[0]+1][shoot_loc[1]]
                    except:
                        break
                    shoot_loc[0] += 1
                if M[shoot_loc[0]][shoot_loc[1]] == '*':
                    M[shoot_loc[0]][shoot_loc[1]] = '.'
            elif d == 'left':
                while M[shoot_loc[0]][shoot_loc[1]] not in ['*', '#']:
                    try:
                        M[shoot_loc[0]][shoot_loc[1]-1] = M[shoot_loc[0]][shoot_loc[1]-1]
                    except:
                        break
                    shoot_loc[1] -= 1
                if M[shoot_loc[0]][shoot_loc[1]] == '*':
                    M[shoot_loc[0]][shoot_loc[1]] = '.'
            elif d == 'right':
                while M[shoot_loc[0]][shoot_loc[1]] not in ['*', '#']:
                    try:
                        M[shoot_loc[0]][shoot_loc[1]+1] = M[shoot_loc[0]][shoot_loc[1]+1]
                    except:
                        break
                    shoot_loc[1] += 1
                if M[shoot_loc[0]][shoot_loc[1]] == '*':
                    M[shoot_loc[0]][shoot_loc[1]] = '.'
    
    # 4. 결과 출력
    result = ''
    for i in range(H):
        result += ''.join(M[i])+'\n'
    print('#{} {}'.format(tc, result))