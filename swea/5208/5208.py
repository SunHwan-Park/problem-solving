import sys
sys.stdin = open('input.txt')

def f(cl, N, arr, cnt):
    global min_cnt
    if cnt >= min_cnt:
        return
    if cl >= N-1:
        if cnt < min_cnt:
            min_cnt = cnt
        return
    
    bat = arr[cl]    
    for i in range(bat-1, -1, -1):
        f(cl+i+1, N, arr, cnt+1)

T = int(input())
for tc in range(1, T+1):
    D = list(map(int, input().split()))
    min_cnt = 10000000
    f(0, D[0], D[1:], 0)
    print('#{} {}'.format(tc, min_cnt-1))