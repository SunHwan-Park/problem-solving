import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    trucks = [list(map(int, input().split())) for _ in range(N)]
    trucks.sort(key=lambda x: x[1])
    end = trucks[0][1]
    count = 1
    for i in range(1, N):
        if end <= trucks[i][0]:
            end = trucks[i][1]
            count += 1
    
    print('#{} {}'.format(tc, count))