import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    a_arr = list(map(int, input().split()))
    b_arr = list(map(int, input().split()))
    
    result = []
    if M > N:
        for i in range(M - N + 1):
            temp = 0
            for j in range(N):
                temp += a_arr[j] * b_arr[j+i]
            result.append(temp)
    else:
        for i in range(N - M + 1):
            temp = 0
            for j in range(M):
                temp += a_arr[j+i] * b_arr[j]
            result.append(temp)
    print('#{} {}'.format(tc, max(result)))