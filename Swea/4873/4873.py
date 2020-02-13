import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    text = input()
    
    stack = [text[0]]
    for i in range(1, len(text)):
        try:
            if text[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(text[i])
        except:
            stack.append(text[i])   
    print('#{} {}'.format(tc, len(stack)))