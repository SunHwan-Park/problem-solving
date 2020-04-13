import sys
sys.stdin = open('input.txt')

from itertools import permutations

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    plus, minus, multiply, division = map(int, input().split())
    numbers = list(map(int, input().split()))

    operator = ['+']*plus + ['-']*minus + ['*']*multiply + ['/']*division
    possible = list(set(permutations(operator, len(operator))))
    
    result = []
    for p_operator in possible:
        current = numbers[0]
        for i in range(len(p_operator)):
            if p_operator[i] == '+':
                current += numbers[i+1]
            elif p_operator[i] == '-':
                current -= numbers[i+1]
            elif p_operator[i] == '*':
                current *= numbers[i+1]
            elif p_operator[i] == '/':
                current = int(current/numbers[i+1])
        result.append(current)
    
    print('#{} {}'.format(tc, max(result)-min(result)))