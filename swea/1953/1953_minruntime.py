import sys
sys.stdin = open('input.txt')

def issafe(row,col):
    return 0<=row<sero and 0<=col<garo
 
def up(row,col):
    if issafe(row-1,col) and not visited[row-1][col] and mymap[row-1][col] in u:
        q.append((row-1,col))
        visited[row-1][col] = 1
        time[row-1][col] = time[row][col]+1
 
def right(row,col):
    if issafe(row,col+1) and not visited[row][col+1] and mymap[row][col+1] in r:
        q.append((row,col+1))
        visited[row][col+1] = 1
        time[row][col+1] = time[row][col]+1
 
def down(row,col):
    if issafe(row+1,col) and not visited[row+1][col] and mymap[row+1][col] in d:
        q.append((row+1,col))
        visited[row+1][col] = 1
        time[row+1][col] = time[row][col]+1
 
def left(row,col):
    if issafe(row,col-1) and not visited[row][col-1] and mymap[row][col-1] in l:
        q.append((row,col-1))
        visited[row][col-1] = 1
        time[row][col-1] = time[row][col]+1
 
 
for tc in range(int(input())):
    sero,garo,row,col,t = map(int,input().split())
    mymap = [[0]*garo for _ in range(sero)]
    for r in range(sero):
        mymap[r] = list(map(int,input().split()))
 
    u = [1,2,5,6]
    r = [1,3,6,7]
    d = [1,2,4,7]
    l = [1,3,4,5]
    visited = [[0]*garo for _ in range(sero)]
    visited[row][col] = 1
    time = [[1]*garo for _ in range(sero)]
 
    q = []
    q.append((row,col))
    cnt = 0
    y = row
    x = col
    while q != []:
        # for i in time:
        #     print(i)
        # print('-'*20)
        # print(cnt)
        y,x = q.pop(0)
        if time[y][x] == t+1:
            break
        cnt += 1
        now = mymap[y][x]
        if now == 1:
            up(y,x)
            right(y, x)
            down(y, x)
            left(y, x)
        elif now == 2:
            up(y, x)
            down(y, x)
        elif now == 3:
            right(y, x)
            left(y, x)
        elif now == 4:
            up(y, x)
            right(y, x)
        elif now == 5:
            right(y, x)
            down(y, x)
        elif now == 6:
            down(y, x)
            left(y, x)
        elif now == 7:
            up(y, x)
            left(y, x)
    print('#{} {}'.format(tc+1,cnt))