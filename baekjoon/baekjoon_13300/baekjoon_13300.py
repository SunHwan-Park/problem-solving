n, k = list(map(int, input().split()))
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))
grade = list(set([matrix[i][1] for i in range(n)]))
arr = [[0 for _ in range(max(grade))] for _ in range(k)]
for i in range(n):
    arr[matrix[i][0]][matrix[i][1]-1] += 1
room = 0
for i in range(k):
    for j in range(len(arr[0])):
        room += arr[i][j]//k + bool(arr[i][j]%k)

print(room)