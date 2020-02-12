matrix = [[0 for _ in range(100)] for _ in range(100)]
n = int(input())
for _ in range(n):
    x, y = list(map(int, input().split()))
    for i in range(x, x+10):
        for j in range(y, y+10):
            matrix[i][j] = 1

answer = 0
for i in range(100):
    answer += sum(matrix[i])
print(answer)