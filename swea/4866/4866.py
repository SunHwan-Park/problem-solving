import sys
sys.stdin = open('input.txt')

T = int(sys.stdin.readline())
for tc in range(1, T+1):
    text = sys.stdin.readline()
    
    bracket1 = ['{', '}']
    bracket2 = ['(', ')']

    answer = 1
    stack = []
    for char in text:
        if char in ['{', '(']:
            stack.append(char)
        elif char in ['}', ')']:
            if stack:
                if char in bracket1:
                    if stack[-1] == bracket1[0]:
                        stack.pop()
                    else:
                        answer = 0
                        break
                else:
                    if stack[-1] == bracket2[0]:
                        stack.pop()
                    else:
                        answer = 0
                        break
            else:
                answer = 0
                break
    if stack:
        answer = 0
    
    print('#{} {}'.format(tc, answer))