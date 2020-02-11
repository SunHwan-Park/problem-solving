N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
arr.sort()
max_high = max([arr[i][1] for i in range(N)])
max_high_idx = [i for i in range(N) if arr[i][1] == max_high]

result = arr[max_high_idx[0]][1]

# 앞에서 부터
left = arr[0][0]
high = arr[0][1] 
for i in range(1, max_high_idx[0]+1):
    if arr[i][1] >= high:
        result += (arr[i][0] - left) * high
        left = arr[i][0]
        high = arr[i][1]

# 뒤에서 부터
left = arr[N-1][0]
high = arr[N-1][1] 
for i in range(N-2, max_high_idx[0]-1, -1):
    if arr[i][1] >= high:
        result += abs((arr[i][0] - left)) * high
        left = arr[i][0]
        high = arr[i][1]

print(result)