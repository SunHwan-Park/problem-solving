import sys
sys.stdin = open('input.txt')

def f(L):
    global result
    for i in range(2):
        if L*2 + i > N:
            return
        elif V[L*2 + i] != 0:
            result += V[L*2 + i]
        else:
            f(L*2 + i)
            
T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    V = [0]*(N+1)
    for _ in range(M):
        node, value = map(int, input().split())
        V[node] = value
    result = 0
    f(L)
    print('#{} {}'.format(tc, result))