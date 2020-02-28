import sys
sys.stdin = open('input.txt')

def dfs(plus, minus, multiply, division, operator_num, stack):
    if operator_num == 0:
        possible.append(stack)
        return
    else:  
        temp = []
        if plus > 0:
            temp.append('+')
        if minus > 0:
            temp.append('-')
        if multiply > 0:
            temp.append('*')
        if division > 0:
            temp.append('/')
        for t in temp:
            if t == '+':
                dfs(plus-1, minus, multiply, division, operator_num-1, stack+t)
            elif t == '-':
                dfs(plus, minus-1, multiply, division, operator_num-1, stack+t)
            elif t == '*':
                dfs(plus, minus, multiply-1, division, operator_num-1, stack+t)
            elif t == '/':
                dfs(plus, minus, multiply, division-1, operator_num-1, stack+t)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    plus, minus, multiply, division = map(int, input().split())
    numbers = list(map(int, input().split()))
    operator_num = plus + minus + multiply + division
    possible = []
    stack = ''
    dfs(plus, minus, multiply, division, operator_num, stack)
    
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