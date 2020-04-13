import sys
sys.stdin = open('input.txt')

def f(box, n, k, S, SS):
    global C, max_profit
    if n == k:
        if SS > max_profit:
            max_profit = SS
    elif S + box[n] > C:
        if SS > max_profit:
            max_profit = SS
    else:
        f(box, n+1, k, S+box[n], SS+(box[n])**2)
        f(box, n+1, k, S, SS)

T = int(input())
for tc in range(1, T+1):
    N, M, C = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    profit = 0
    for i in range(N):
        for j in range(N-M+1):
            box1 = matrix[i][j:j+M]
            for k in range(N):
                for l in range(N-M+1):
                    if k != i or l >= j+M:
                        box2= matrix[k][l:l+M]
                        
                        max_profit = 0
                        f(box1, 0, len(box1), 0, 0)
                        box1_profit = max_profit
                        max_profit = 0
                        f(box2, 0, len(box2), 0, 0)
                        box2_profit = max_profit
                        total_profit = box1_profit + box2_profit
                        if profit < total_profit:
                            profit = total_profit
    
    print('#{} {}'.format(tc, profit))