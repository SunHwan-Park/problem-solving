def f(n, k, s):
    global minV
    if n == k: # 순열 1개 완성
        if minV > s:
            minV = s # 재귀 안에 for문 만 줄여도 빨라진다
    elif minV <= s:
        return
    else:
        for i in range(k): # used를 왼쪽부터 탐색 (사용할 수 있는 숫자 검색)
            if u[i] == 0: # 이미 사용한 숫자가 아니면
                u[i] = 1
                p[n] = i
                f(n+1, k, s+arr[n][i]) # 다음 자리를 결정하러 이동
                u[i] = 0

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    p = [0]*N
    u = [0]*N
    minV = 10*N
    f(0, N, 0)
    print('#{} {}'.format(tc, minV))