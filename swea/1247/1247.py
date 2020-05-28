import sys
sys.stdin = open('input.txt')

def f(n, cx, cy, cost):
    global result, N, house
    if cost >= result:
        return
    elif n == N:
        new_cost = cost + abs(cx-house[0]) + abs(cy-house[1])
        if result > new_cost:
            result = new_cost
    else:
        for i in range(N):
            if V[i] == 0:
                V[i] = 1
                nx = customers[i][0]
                ny = customers[i][1]
                f(n+1, nx, ny, cost+abs(cx-nx)+abs(cy-ny))
                V[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    D = list(map(int, input().split()))
    office = (D[0], D[1])
    house = (D[2], D[3])
    customers = [(D[2*i+4], D[2*i+5]) for i in range(N)]
    customers.sort(key=lambda x: x[0]+x[1])
    V = [0]*N
    result = sum(D)
    f(0, office[0], office[1], 0)
    print('#{} {}'.format(tc, result))