isp = {'*':2, '/':2, '+':1, '-':1, '(':0}
icp = {'*':2, '/':2, '+':1, '-':1, '(':3}

def to_b(D):
    stack = []
    result = ''
    for d in D:
        try:
            if d in isp.keys():
                if isp[stack[-1]] >= icp[d]:
                    while isp[stack[-1]] >= icp[d]:
                        result += stack.pop()
                    stack.append(d)
                else:
                    stack.append(d)
            elif d == ')':
                while stack[-1] != '(':
                    result += stack.pop()
                stack.pop()
            else:
                result += d
        except:
            stack.append(d)
    
    while stack:
        result += stack.pop()
    
    return result

def to_m(D):
    stack = []
    for d in D:
        if d in isp.keys():
            if d == '+':
                stack.append(stack.pop() + stack.pop())
            elif d == '-':
                stack.append(stack.pop() - stack.pop())
            elif d == '*':
                stack.append(stack.pop() * stack.pop())
            elif d == '/':
                stack.append(stack.pop() / stack.pop())
        else:
            stack.append(int(d))
    return stack[0]

import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    D = input()

    print('#{} {}'.format(tc, to_m(to_b(D))))