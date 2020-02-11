K = int(input())
arr = [[-1, -1]]
for _ in range(6):
    arr.append(list(map(int, input().split())))

max_length = 0
max_width = 0
result = 0
exception = 1
for i in range(1, 7):
    if arr[i][0] in [1, 2]:
        if arr[i][1] > max_length:
            max_length = arr[i][1]
    elif arr[i][0] in [3, 4]:
        if arr[i][1] > max_width:
            max_width = arr[i][1]

    if (arr[i-1][0], arr[i][0]) in [(1, 3), (2, 4), (3, 2), (4, 1)]:
        result -= arr[i-1][1] * arr[i][1]
        exception -= 1

if exception:
    result -= arr[1][1]*arr[-1][1]
result += max_length * max_width

print(result*K)