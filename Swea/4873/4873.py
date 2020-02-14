import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    text = input()
    
    stack = []
    for i in range(len(text)):
        try:
            if text[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(text[i])
        except:
            stack.append(text[i])   
    print('#{} {}'.format(tc, len(stack)))

# -------------------------------
# 강사님 코드
T = int(input())
for tc in range(1, T+1):
    stack = []
    D = input()
    for c in D:
        if stack:
            if stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
        else:
            stack.append(c)
    print('#{} {}'.format(tc, len(stack)))