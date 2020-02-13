import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    matrix = []
    for _ in range(N):
        matrix.append([0 for _ in range(M-1)] + list(map(int, input().split())) + [0 for _ in range(M-1)])
    for _ in range(N-1):
        matrix.insert(0, [0 for _ in range(3*M-2)])
        matrix.append([0 for _ in range(3*M-2)])
    
    max_count = 0
    for i in range(N-1, 2*N-1):
        for j in range(M-1, 2*M-1):
            length = matrix[i][j]
            count = -matrix[i][j]
            for k in range(-length, length+1):
                count += matrix[i+k][j]
                count += matrix[i][j+k]
            if count > max_count:
                max_count = count
    
    print('#{} {}'.format(tc, max_count))

# ---------------------------------------
# 조진환 코드
for t in range(int(input())):
    N,M=map(int,input().split())
    arr=[list(map(int,input().split())) for _ in range(N)]
    dx=[0,0,-1,1]
    dy=[-1,1,0,0]
    mx=0
    for i in range(N): # 모든점 
        for j in range(M):
            long=arr[i][j]
            total=arr[i][j]
            for k in range(4):
                for l in range(1,long+1):
                    if 0<=i+l*dx[k]<N and 0<=j+l*dy[k]<M:
                        total+=arr[i+l*dx[k]][j+l*dy[k]]
            if total>mx:
                mx=total
             
    print('#{} {}'.format(t+1,mx))