import sys
T = int(sys.stdin.readline())
for _ in range(T):
    data = sys.stdin.readline().strip()
    while True:
        if '()' in data:
            data = data.replace('()', '')
        else:
            break
    if data:
        print('NO')
    else:
        print('YES')

# ---------------------------------
# 강사님 코드
import sys
T = int(sys.stdin.readline())

for _ in range(T):
    D = list(sys.stdin.readline().strip())
    stack = [] # stack을 숫자로 두고, 경우에 따라 더하기 빼기로 해도 가능!
    for p in D:
        if p == '(':
            stack.append(p)
        else:
            if stack:
                stack.pop()
            else:
                print('NO')
                break
    else: # break 안 만나고 for문 다 돌면 실행되는 경우!
        if stack:
            print('NO')
        else:
            print('YES')