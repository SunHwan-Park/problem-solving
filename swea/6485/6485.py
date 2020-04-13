import sys
sys.stdin = open('input.txt')

#1. test data 입력
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    P = int(input())
    C = [[], []]
    for _ in range(P):
        C[0].append(int(input()))
        C[1].append(0)

    #2. 각 노선별 지나가는 정류장
    for i in range(N): # 각 노선별
        for j in range(P): # 각 정류장이
            if C[0][j] in range(A[i], B[i]+1): # 해당 노선에 포함된다면
                C[1][j] += 1 # 해당 정류장에 +1
    
    #3. 결과 출력
    print('#{} {}'.format(tc, ' '.join(map(str, C[1]))))