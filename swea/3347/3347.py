import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    V = [0]*N
    for b in B:
        for i in range(N):
            if A[i] <= b:
                V[i] += 1
                break
    print('#{} {}'.format(tc, V.index(max(V)) + 1))