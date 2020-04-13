for _ in range(10):
    tc = int(input())
    maze = [list(map(int, list(input()))) for _ in range(16)]
 
    for i in range(16):
        if 2 in maze[i]:
            sx = i
            sy = maze[i].index(2)
        if 3 in maze[i]:
            gx = i
            gy = maze[i].index(3)
 
    stack =[[sx, sy]]
 
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    result = 0
    while stack:
        x, y = stack.pop()
        maze[x][y] = 1
        if x == gx and y == gy:
            result = 1
            break
        else:
            for i in range(4):
                if maze[x+dx[i]][y+dy[i]] == 0 or maze[x+dx[i]][y+dy[i]] == 3:
                    stack.append([x+dx[i], y+dy[i]])
 
    print(f'#{tc} {result}')