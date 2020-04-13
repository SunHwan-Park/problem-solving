T = int(input())
 
for tc in range(1, T+1):
    fare = list(map(int, input().split()))
    d = list(map(int, input().split()))
    dp = [0]*12
    dp[0] = min(fare[0]*d[0], fare[1])
    for i in range(1, 12):
        dp[i] = min(dp[i-1]+d[i]*fare[0], dp[i-1]+fare[1])
        if i >= 2:
            dp[i] = min(dp[i-3]+fare[2], dp[i])
    result = min(dp[11], fare[3])
    print(f'#{tc} {result}')