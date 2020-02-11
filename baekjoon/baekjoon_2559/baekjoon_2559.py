N, K = list(map(int, input().split()))
arr = list(map(int, input().split()))

current_sum = sum(arr[0:K])
max_sum = current_sum

for i in range(N - K):
    current_sum = current_sum - arr[i] + arr[i+K]
    if current_sum > max_sum:
        max_sum = current_sum

print(max_sum)