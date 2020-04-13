import sys
sys.stdin = open('input.txt')

#1. test data 입력
T = int(input())
for tc in range(1, T+1):
    data = input().split()

    # 2. 스택 생성, 후위표기식을 중위 표기식으로 변환
    stack = []
    for d in data:
        try:
            if d in ['+', '-', '/', '*']: # 연산자일 때
                back = stack.pop()
                front = stack.pop()
                if d == '+':
                    stack.append(front + back)
                elif d == '-':
                    stack.append(front - back)
                elif d == '/':
                    stack.append(int(front / back)) # float -> int 형 변환
                elif d == '*':
                    stack.append(front * back)
            elif d == '.':
                result = stack.pop() # 마지막 결과를 result로
            else:
                stack.append(int(d))
        except: # 중간에 에러가 나는 경우, result를 'error'로
            result = 'error'
            break

    if stack: # 스택이 비어있지 않다면
        print('#{} {}'.format(tc, 'error'))
    else:
        print('#{} {}'.format(tc, result))