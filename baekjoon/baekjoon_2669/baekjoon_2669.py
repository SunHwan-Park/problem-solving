data = [list(map(int, input().split())) for _ in range(4)]
n = max([max(data[i]) for i in range(4)])
matrix = [[0 for _ in range(n)] for _ in range(n)]

for d in data:
    for i in range(d[0], d[2]):
        for j in range(d[1], d[3]):
            matrix[i][j] += 1
result = n*n
for i in range(n):
    result -= matrix[i].count(0)
print(result)