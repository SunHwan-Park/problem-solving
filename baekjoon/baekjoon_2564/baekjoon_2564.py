col, row = list(map(int, input().split()))
n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
x_loc = list(map(int, input().split()))

result = 0
for d in data:
    if d[0] == x_loc[0]:
        result += abs(x_loc[1] - d[1])
    elif d[0] + x_loc[0] == 3:
        result += min(d[1]+x_loc[1]+row, 2*col+row-d[1]-x_loc[1])
    elif d[0] + x_loc[0] == 4:
        result += d[1] + x_loc[1]
    elif d[0] + x_loc[0] == 5:
        if x_loc[0] == 1:
            result += col + d[1] - x_loc[1]
        elif x_loc[0] == 4:
            result += col - d[1] + x_loc[1]
        elif x_loc[0] == 2:
            result += row - d[1] + x_loc[1]
        elif x_loc[0] == 3:
            result += row + d[1] - x_loc[1]
    elif d[0] + x_loc[0] == 6:
        result += col + row - d[1] - x_loc[1]
    elif d[0] + x_loc[0] == 7:
        result += min(d[1]+x_loc[1]+col, 2*row+col-d[1]-x_loc[1])

print(result)