from itertools import combinations
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    C = [list(map(int, input().split())) for _ in range(N)]
    
    R = []
    H = []
    for i in range(N):
        for j in range(N):
            if C[i][j] == 1:
                H.append((i, j))
            if C[i][j] >= 2:
                R.append((i, j))
    
    answer = N**3
    for i in range(len(R)):
        combies = combinations(R, i + 1)
        for combi in combies:
            cost = 0
            for ur in combi:
                cost += C[ur[0]][ur[1]]
            if cost >= answer:
                continue

            total_D = 0
            for uh in H:
                min_D = N*N
                for ur in combi:
                    D = abs(uh[0] - ur[0]) + abs(uh[1] - ur[1])
                    if D < min_D:
                        min_D = D
                total_D += min_D
                if cost + total_D >= answer:
                    break
                
            if answer > cost + total_D:
                answer = cost + total_D
    
    print('#{} {}'.format(tc, answer))