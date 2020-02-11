n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))
pair = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}

max_result = 0
for i in range(6):
    result = 0
    low = matrix[0][i]
    high = matrix[0][pair[i]]
    result += max(set(range(1, 7)) - set([low, high]))
    for j in range(1, n):
        low = high
        high = matrix[j][pair[matrix[j].index(low)]]
        result += max(set(range(1, 7)) - set([low, high]))
    if result > max_result:
        max_result = result
print(max_result)