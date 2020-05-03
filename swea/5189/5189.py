import sys
sys.stdin = open('input.txt')

from itertools import permutations

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    possible = list(permutations(range(1, N), N-1))
    result = 1000000000
    for p in possible:
        temp = matrix[0][p[0]] + matrix[p[-1]][0]
        for i in range(N-2):
            if temp >= result:
                break
            temp += matrix[p[i]][p[i+1]]
        if temp < result:
            result = temp
    print('#{} {}'.format(tc, result))