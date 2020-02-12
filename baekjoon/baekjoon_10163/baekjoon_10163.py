matrix = [[0 for _ in range(101)] for _ in range(101)]
N = int(input())
for k in range(1, N+1):
    box_x, box_y, length, width = list(map(int, input().split()))
    for i in range(box_x, box_x+length):
        for j in range(box_y, box_y+width):
            matrix[i][j] = k

for k in range(1, N+1):
    result = 0
    for i in range(101):
        result += matrix[i].count(k)
    print(result)